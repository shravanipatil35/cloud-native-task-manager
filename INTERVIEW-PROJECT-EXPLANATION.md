# Interview Explanation: Cloud-Native Task Manager

## Project Summary

The Cloud-Native Task Manager is a web application with a Flask API, static Nginx frontend, and PostgreSQL database. I use Docker Compose for local development, Terraform for AWS infrastructure, Kubernetes on EKS for deployment, and Jenkins to build, test, publish, and deploy application images.

## Architecture

- The browser loads the Task Manager UI from Nginx.
- Nginx forwards `/api/` requests to the Flask backend.
- Flask stores application data in PostgreSQL.
- In Kubernetes, the frontend is exposed through a LoadBalancer Service, the backend and database use internal Services, and PostgreSQL data is stored on a persistent volume claim.
- Terraform provisions the VPC, subnets, EC2 host, EKS cluster, managed node group, and associated IAM/network permissions.

## Delivery Flow

1. Jenkins checks out the repository and builds backend and frontend container images.
2. Jenkins starts the Compose application with credentials supplied through Jenkins and checks the frontend and backend health endpoints.
3. Jenkins pushes build-number-tagged images to the configured Docker Hub namespace.
4. Jenkins connects to the selected EKS cluster, creates runtime Kubernetes Secrets from Jenkins credentials, deploys PostgreSQL and the application, and waits for rollout completion.

## Security and Operations

Credentials are configured locally in `.env` or in Jenkins Credentials; no usable password, session key, AWS access key, or private key is committed. Terraform state and local variable files are ignored by Git. EC2 SSH and Jenkins ingress are disabled until an operator supplies restricted CIDRs. AWS resources, especially EKS and NAT gateways, should be destroyed when a disposable environment is no longer needed.

The PostgreSQL claim uses the AWS EBS CSI add-on. The optional Ingress resource requires an ingress controller for its configured class; the frontend LoadBalancer Service can be used without it.

## Short Interview Version

“I built a Task Manager application with a Flask API, Nginx frontend, and PostgreSQL. I containerized the services and use Compose locally. Terraform provisions the AWS network and EKS environment, while Kubernetes runs the application and persistent database. A Jenkins pipeline builds and checks the containers, pushes versioned images, and deploys them to EKS using credentials stored in Jenkins rather than in the repository.”
