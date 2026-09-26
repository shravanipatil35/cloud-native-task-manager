# DevOps Files Explained

This guide describes the files that make up the Cloud-Native Task Manager deployment. The stack is intentionally limited to the application, PostgreSQL, Docker/Compose, AWS/Terraform, Kubernetes, and Jenkins.

## Application Containers

- `backend/Dockerfile` installs the Python requirements and starts the Flask API after the PostgreSQL host is reachable.
- `frontend/Dockerfile` packages the existing static UI in Nginx. `frontend/nginx.conf` serves the pages and proxies `/api/` requests to the backend service.
- `docker-compose.yml` runs PostgreSQL, the Flask backend, and the frontend for local development. It reads the database password and Flask session key from the ignored `.env` file; `.env.example` contains variable names but no usable credentials.

## Kubernetes (`k8s/`)

- `namespace.yaml` creates the `taskmanager` namespace.
- `storage-class.yaml` defines the EBS CSI-backed `gp3` storage class; `postgres-pvc.yaml` requests persistent storage for PostgreSQL.
- `postgres-deployment.yaml` runs PostgreSQL and exposes it internally as a ClusterIP Service.
- `backend-deployment.yaml` runs Flask, obtains the app key and database password from Kubernetes Secrets, and defines health probes and a ClusterIP Service.
- `frontend-deployment.yaml` runs Nginx and exposes it through a LoadBalancer Service.
- `ingress.yaml` optionally routes HTTP traffic for `taskmanager.local` through an ingress controller configured for the `nginx` class.

Secret values are deliberately not stored in a Kubernetes YAML file. Jenkins creates `postgres-secret` and `backend-secret` from Jenkins credentials during deployment. For manual deployment, create Secrets with the same names and keys in the `taskmanager` namespace using a secure local process.

## Jenkins (`Jenkinsfile`)

The declarative pipeline checks out the repository, builds images tagged with the build number, runs the Compose stack and HTTP checks, pushes images, and deploys them to EKS. It creates the namespace-scoped runtime Secrets, waits for the EBS CSI add-on and database, applies the application workloads, updates image tags, and verifies rollouts.

Configure these Jenkins credentials before running a build:

- `dockerhub-credentials`: username/password credential for the selected Docker Hub namespace
- `aws-credentials`: AWS credentials allowed to update kubeconfig and deploy to the cluster
- `taskmanager-db-password`: secret text for PostgreSQL
- `taskmanager-app-secret-key`: secret text used to sign Flask sessions

Set the `DOCKERHUB_NAMESPACE`, `AWS_REGION`, and `EKS_CLUSTER_NAME` build parameters. The Jenkins agent needs Docker, Compose v2, AWS CLI, `kubectl`, and `curl`.

## Terraform (`terraform/`)

- `vpc.tf` creates the VPC, public/private subnets, internet gateway, NAT gateway, and routes.
- `security-groups.tf` configures EC2 and EKS network access. SSH and Jenkins access are closed unless CIDRs are provided in `allowed_ssh_cidrs`.
- `eks.tf` creates the EKS cluster, managed node group, IAM roles, and required policies, including EBS CSI permissions.
- `ec2.tf` creates the configured EC2 host and imports its public key.
- `variables.tf` contains configurable region, networking, EC2, and EKS values. `terraform.tfvars.example` is a template; local `terraform.tfvars` and state files are ignored.
- `outputs.tf` reports resource identifiers and connection commands.

Review AWS charges and the Terraform plan before applying. EKS, EC2, NAT gateways, load balancers, and persistent storage can incur charges.

## Jenkins Kubernetes Files

`jenkins/jenkins-deployment.yaml` and `jenkins/jenkins-rbac.yaml` are optional Kubernetes resources for running Jenkins in a cluster. They are separate from the application deployment; the pipeline can also run on an external Jenkins controller and agent.
