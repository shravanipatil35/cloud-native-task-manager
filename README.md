#  Cloud-Native Task Manager – Complete DevOps Platform

A full-stack Task Manager web application demonstrating an end-to-end DevOps workflow using **Flask, PostgreSQL, Docker, Kubernetes, AWS EKS, Terraform, Jenkins, and Docker Hub**.

The project demonstrates how an application can be developed locally, containerized with Docker, infrastructure can be provisioned using Infrastructure as Code, the application can be deployed to Kubernetes on AWS EKS, and the complete build/test/deployment process can be automated using Jenkins CI/CD.

This project is designed as a practical DevOps portfolio project covering:

* Full-stack web application deployment
* Containerization with Docker
* Local multi-container development with Docker Compose
* Infrastructure as Code with Terraform
* AWS networking and compute
* Kubernetes orchestration
* Amazon EKS
* Persistent PostgreSQL storage
* Jenkins CI/CD automation
* Docker Hub image publishing
* Kubernetes rolling deployments
* Application health checks
* Secrets and environment-variable management
* Troubleshooting and operational workflows

---

#  Table of Contents

1. [Project Overview](#-project-overview)
2. [Key Features](#-key-features)
3. [System Architecture](#-system-architecture)
4. [Architecture Components](#-architecture-components)
5. [Technology Stack](#-technology-stack)
6. [Project Workflow](#-project-workflow)
7. [Application Data Flow](#-application-data-flow)
8. [Repository Structure](#-repository-structure)
9. [Prerequisites](#-prerequisites)
10. [Local Development with Docker Compose](#-local-development-with-docker-compose)
11. [Docker Architecture](#-docker-architecture)
12. [AWS Infrastructure with Terraform](#-aws-infrastructure-with-terraform)
13. [AWS Networking Architecture](#-aws-networking-architecture)
14. [EC2 Infrastructure](#-ec2-infrastructure)
15. [Amazon EKS](#-amazon-eks)
16. [Kubernetes Architecture](#-kubernetes-architecture)
17. [PostgreSQL Persistent Storage](#-postgresql-persistent-storage)
18. [Jenkins CI/CD Pipeline](#-jenkins-cicd-pipeline)
19. [Complete CI/CD Flow](#-complete-cicd-flow)
20. [Environment Variables and Secrets](#-environment-variables-and-secrets)
21. [Security Practices](#-security-practices)
22. [Deployment Verification](#-deployment-verification)
23. [Troubleshooting Guide](#-troubleshooting-guide)
24. [Important Commands](#-important-commands)
25. [Useful Kubernetes Commands](#-useful-kubernetes-commands)
26. [Terraform Commands](#-terraform-commands)
27. [AWS CLI Commands](#-aws-cli-commands)
28. [Project Limitations](#-project-limitations)
29. [Future Improvements](#-future-improvements)
30. [Contributing](#-contributing)
31. [Project Summary](#-project-summary)

---

#  Project Overview

## What is this Project?

Cloud-Native Task Manager is a task-management web application deployed using modern DevOps practices.

The application consists of three main runtime components:

1. **Frontend**

   * Static HTML/CSS/JavaScript application
   * Served by Nginx
   * Exposed on port `80`

2. **Backend**

   * Flask-based Python API
   * Handles application logic and database operations
   * Runs using Gunicorn
   * Exposed internally on port `8888`

3. **PostgreSQL**

   * Relational database
   * Stores application data
   * Runs as a Kubernetes workload
   * Uses persistent EBS-backed storage in AWS

The application can run locally using Docker Compose and can be deployed to AWS EKS using Kubernetes.

---

#  Key Features

### Application

* Task management interface
* User authentication
* Task creation and management
* Flask REST API
* PostgreSQL database
* Password hashing
* Health endpoints

### Containerization

* Separate frontend and backend Docker images
* PostgreSQL container for local development
* Docker Compose for local orchestration
* Gunicorn application server
* Nginx frontend server
* Database startup handling

### Infrastructure

* AWS VPC
* Public and private subnets
* Internet Gateway
* NAT Gateway
* Route tables
* EC2 instance
* Security Groups
* IAM roles
* Amazon EKS
* Managed EKS node group

### Kubernetes

* Namespace isolation
* Deployments
* Services
* PostgreSQL persistent storage
* StorageClass
* PersistentVolumeClaim
* Health probes
* Resource requests and limits
* RollingUpdate strategy
* LoadBalancer service
* Optional Nginx Ingress

### CI/CD

* Jenkins pipeline
* Docker image builds
* Docker Compose integration testing
* Docker Hub publishing
* AWS EKS deployment
* Kubernetes rollout verification
* Build-number image tagging

---

#  System Architecture

## High-Level Architecture

```text
                         ┌──────────────────────┐
                         │       Developer      │
                         │   Code / Git Push    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │       GitHub         │
                         │   Source Repository  │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │       Jenkins        │
                         │      CI/CD Server    │
                         └──────────┬───────────┘
                                    │
                ┌───────────────────┼───────────────────┐
                │                   │                   │
                ▼                   ▼                   ▼
        ┌───────────────┐   ┌───────────────┐   ┌───────────────┐
        │ Docker Build  │   │ Docker Compose │   │ Docker Hub    │
        │ Backend       │   │ Integration    │   │ Image Registry│
        │ Frontend      │   │ Test           │   │               │
        └───────────────┘   └───────────────┘   └───────┬───────┘
                                                        │
                                                        ▼
                                           ┌──────────────────────┐
                                           │      AWS EKS         │
                                           │    Kubernetes         │
                                           └──────────┬───────────┘
                                                      │
                         ┌────────────────────────────┼──────────────────────┐
                         │                            │                      │
                         ▼                            ▼                      ▼
                ┌─────────────────┐        ┌─────────────────┐      ┌─────────────────┐
                │ Frontend Pods   │        │ Backend Pod     │      │ PostgreSQL Pod  │
                │ Nginx           │        │ Flask/Gunicorn  │      │ PostgreSQL 15   │
                │ Port 80         │        │ Port 8888       │      │ Port 5432       │
                └────────┬────────┘        └────────┬────────┘      └────────┬────────┘
                         │                          │                         │
                         │                          └──────────┬──────────────┘
                         │                                     │
                         ▼                                     ▼
                ┌─────────────────┐                  ┌────────────────────┐
                │ LoadBalancer    │                  │ EBS Persistent     │
                │ Service         │                  │ Storage            │
                └─────────────────┘                  └────────────────────┘
```

Terraform provisions the AWS infrastructure required for EKS, networking, EC2, IAM, and security groups.

Jenkins handles the application CI/CD workflow.

Kubernetes handles application deployment and runtime orchestration.

---

#  Architecture Components

| Component               | Purpose                         | Technology            |
| ----------------------- | ------------------------------- | --------------------- |
| Frontend                | Web interface                   | HTML, CSS, JavaScript |
| Web Server              | Serves frontend                 | Nginx                 |
| Backend                 | REST API and application logic  | Flask/Python          |
| Application Server      | Runs Flask application          | Gunicorn              |
| Database                | Persistent application data     | PostgreSQL 15         |
| Containerization        | Package applications            | Docker                |
| Local Orchestration     | Run services locally            | Docker Compose        |
| Infrastructure          | Provision AWS resources         | Terraform             |
| Cloud                   | Infrastructure platform         | AWS                   |
| Container Orchestration | Run containers                  | Kubernetes            |
| Kubernetes Platform     | Managed Kubernetes              | Amazon EKS            |
| Image Registry          | Store Docker images             | Docker Hub            |
| CI/CD                   | Build and deployment automation | Jenkins               |
| Persistent Storage      | PostgreSQL storage              | Amazon EBS / EBS CSI  |

---

#  Technology Stack

## Backend

```text
Language:          Python 3.11
Framework:         Flask 3.0.0
ORM:               Flask-SQLAlchemy / SQLAlchemy
Database Driver:   psycopg2-binary
Application Server: Gunicorn
CORS:              Flask-CORS
Configuration:     python-dotenv
```

The current backend dependencies include Flask, Flask-SQLAlchemy, Flask-CORS, python-dotenv, SQLAlchemy, Werkzeug, psycopg2-binary, and Gunicorn.

## Frontend

```text
HTML5
CSS3
JavaScript
Nginx
```

## DevOps and Infrastructure

```text
Docker
Docker Compose
Kubernetes
Amazon EKS
Terraform
Jenkins
Docker Hub
AWS CLI
kubectl
```

## AWS Services

```text
Amazon VPC
Internet Gateway
NAT Gateway
Elastic IP
EC2
Amazon EKS
EKS Managed Node Group
IAM
Security Groups
Amazon EBS
EBS CSI Driver
```

---

#  Project Workflow

## Complete End-to-End Workflow

```text
Developer
    │
    │ git push
    ▼
GitHub
    │
    │ Jenkins checkout
    ▼
Jenkins
    │
    ├── Checkout
    │
    ├── Build Docker Images
    │
    ├── Docker Compose Test
    │
    ├── Push Images to Docker Hub
    │
    └── Deploy to EKS
              │
              ▼
        Kubernetes Cluster
              │
       ┌──────┼───────┐
       ▼      ▼       ▼
   Frontend Backend PostgreSQL
```

---

#  Jenkins Pipeline Workflow

The current Jenkins pipeline contains five main stages:

```text
Stage 1 → Checkout
Stage 2 → Build Images
Stage 3 → Test with Docker Compose
Stage 4 → Push Images
Stage 5 → Deploy to EKS
```

## Stage 1 – Checkout

Jenkins checks out the source code configured by the Jenkins SCM job.

```groovy
checkout scm
```

This ensures the pipeline works with the current repository contents.

---

## Stage 2 – Build Images

Jenkins builds two Docker images:

```text
Backend:
<namespace>/taskmanager-backend:<BUILD_NUMBER>

Frontend:
<namespace>/taskmanager-frontend:<BUILD_NUMBER>
```

The build number is used as the image tag rather than relying only on `latest`.

Example:

```text
taskmanager-backend:15
taskmanager-frontend:15
```

This makes each Jenkins build identifiable.

---

## Stage 3 – Test with Docker Compose

Jenkins starts the complete local application stack:

```bash
docker compose up -d --build
```

The pipeline then checks:

```text
Backend:
http://localhost:8888/api/health

Frontend:
http://localhost/
```

The backend health endpoint is retried until it becomes available.

The pipeline cleans up the temporary Compose environment after the stage.

---

## Stage 4 – Push Images

Jenkins authenticates to Docker Hub using Jenkins credentials.

The password is passed through standard input:

```bash
printf '%s' "$DOCKER_PASS" | docker login \
  -u "$DOCKER_USER" \
  --password-stdin
```

Then both images are pushed:

```bash
docker push <namespace>/taskmanager-backend:$BUILD_NUMBER
docker push <namespace>/taskmanager-frontend:$BUILD_NUMBER
```

---

## Stage 5 – Deploy to EKS

Jenkins first configures Kubernetes access:

```bash
aws eks update-kubeconfig \
  --name "$EKS_CLUSTER_NAME" \
  --region "$AWS_REGION"
```

Then it applies the Kubernetes resources.

The pipeline also ensures that the AWS EBS CSI add-on exists because PostgreSQL requires persistent EBS-backed storage.

After that:

```text
Namespace
   ↓
StorageClass
   ↓
Secrets
   ↓
PostgreSQL PVC
   ↓
PostgreSQL Deployment
   ↓
Backend Deployment
   ↓
Frontend Deployment
   ↓
Ingress
   ↓
Update Docker images
   ↓
Wait for rollouts
```

---

#  Application Data Flow

```text
                    USER
                     │
                     │ HTTP
                     ▼
             ┌───────────────┐
             │    Nginx      │
             │   Frontend    │
             │    :80        │
             └───────┬───────┘
                     │
                     │ /api
                     ▼
             ┌───────────────┐
             │ Flask Backend │
             │   Gunicorn    │
             │    :8888      │
             └───────┬───────┘
                     │
                     │ SQL
                     ▼
             ┌───────────────┐
             │  PostgreSQL   │
             │    :5432      │
             └───────────────┘
```

The frontend is served by Nginx.

API requests are handled by the Flask backend.

The backend communicates with PostgreSQL.

---

#  Repository Structure

```text
cloud-native-task-manager/
│
├── backend/
│   ├── app/
│   │   ├── ...
│   │
│   ├── static/
│   ├── templates/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── run.py
│   ├── wait-for-db.sh
│   └── .dockerignore
│
├── frontend/
│   ├── ...
│   ├── Dockerfile
│   ├── nginx.conf
│   └── .dockerignore
│
├── k8s/
│   ├── namespace.yaml
│   ├── storage-class.yaml
│   ├── postgres-pvc.yaml
│   ├── postgres-deployment.yaml
│   ├── backend-deployment.yaml
│   ├── frontend-deployment.yaml
│   └── ingress.yaml
│
├── terraform/
│   ├── provider.tf
│   ├── variables.tf
│   ├── vpc.tf
│   ├── security-groups.tf
│   ├── ec2.tf
│   ├── eks.tf
│   ├── terraform.tfvars.example
│   ├── README.md
│   └── keys/
│
├── jenkins/
│   └── jenkins-deployment.yaml
│
├── Jenkinsfile
├── docker-compose.yml
├── .env.example
├── .gitignore
├── DEVOPS-FILES-EXPLAINED.md
├── INTERVIEW-PROJECT-EXPLANATION.md
└── PROJECT-QUESTION-BANK.md
```

---

#  Prerequisites

## Local Machine

Install:

```text
Git
Docker
Docker Compose v2
Python 3.11+
AWS CLI
kubectl
Terraform 1.5+
```

For Jenkins deployment, the Jenkins agent additionally needs:

```text
Docker
Docker Compose v2
AWS CLI
kubectl
curl
```

---

#  Local Development with Docker Compose

## Quick Start

Clone the repository:

```bash
git clone https://github.com/shravanipatil35/cloud-native-task-manager.git
cd cloud-native-task-manager
```

Create the environment file:

```bash
cp .env.example .env
```

Set:

```text
POSTGRES_PASSWORD=<your-password>
SECRET_KEY=<your-random-secret>
```

A secure Flask secret can be generated with:

```bash
python -c "import secrets; print(secrets.token_urlsafe(48))"
```

Do not commit `.env`.

---

## Start the Application

```bash
docker compose up --build
```

The local architecture is:

```text
Frontend
localhost:80
     │
     ▼
Backend
localhost:8888
     │
     ▼
PostgreSQL
localhost:5432
```

Open:

```text
http://localhost
```

Backend health endpoint:

```text
http://localhost:8888/api/health
```

---

## Check Running Containers

```bash
docker compose ps
```

---

## View Logs

All services:

```bash
docker compose logs -f
```

Backend:

```bash
docker compose logs -f backend
```

Frontend:

```bash
docker compose logs -f frontend
```

PostgreSQL:

```bash
docker compose logs -f postgres
```

---

## Stop the Application

```bash
docker compose down
```

The named PostgreSQL volume is retained.

To remove the database volume:

```bash
docker compose down -v
```

Use `-v` only when intentionally deleting local PostgreSQL data.

---

#  Docker Architecture

## Backend Dockerfile

The backend uses:

```dockerfile
FROM python:3.11-slim
```

The Dockerfile:

1. Creates `/app`
2. Installs Python dependencies
3. Copies application code
4. Installs `netcat-openbsd`
5. Adds the database wait script
6. Exposes port `8888`
7. Starts through `wait-for-db.sh`

The application is ultimately served using Gunicorn.

---

## Frontend Dockerfile

The frontend uses:

```dockerfile
FROM nginx:alpine
```

The static frontend is copied to:

```text
/usr/share/nginx/html
```

The custom Nginx configuration is copied to:

```text
/etc/nginx/conf.d/default.conf
```

Nginx listens on:

```text
Port 80
```

---

#  Docker Compose Architecture

The Compose file defines three services:

```text
postgres
backend
frontend
```

## PostgreSQL

```yaml
image: postgres:15-alpine
```

It uses the named volume:

```text
postgres_data
```

mounted at:

```text
/var/lib/postgresql/data
```

A PostgreSQL health check uses:

```bash
pg_isready
```

---

## Backend

The backend is built from:

```text
./backend
```

It connects to PostgreSQL using:

```text
DB_HOST=postgres
```

This works because Docker Compose provides internal DNS using service names.

---

## Frontend

The frontend is built from:

```text
./frontend
```

and exposed through:

```text
80:80
```

---

#  AWS Infrastructure with Terraform

Terraform provisions the AWS infrastructure.

The current Terraform configuration includes:

```text
VPC
Internet Gateway
Public Subnets
Private Subnets
NAT Gateway
Elastic IP
Route Tables
Security Group
EC2
IAM Roles
EKS Cluster
EKS Managed Node Group
```

Terraform uses reusable variables rather than embedding environment-specific AWS values directly into the infrastructure code.

---

#  Terraform Files

## `provider.tf`

Defines:

* Terraform version requirement
* AWS provider
* AWS region
* Default resource tags

Example tags:

```text
Project
Environment
ManagedBy
```

Remote S3 state configuration is documented as an optional configuration for shared environments.

---

## `variables.tf`

Important variables include:

```text
project_name
environment
aws_region
vpc_cidr
public_subnet_cidrs
private_subnet_cidrs
availability_zones

ec2_ami_id
ec2_instance_type
ec2_key_pair_name
ec2_volume_size

eks_cluster_name
eks_cluster_version
eks_public_access_cidrs

eks_node_instance_types
eks_node_desired
eks_node_min
eks_node_max

allowed_ssh_cidrs
```

The configuration requires at least two Availability Zones for EKS.

---

#  Terraform Deployment

Go to:

```bash
cd terraform
```

Initialize:

```bash
terraform init
```

Format:

```bash
terraform fmt
```

Validate:

```bash
terraform validate
```

Review the infrastructure:

```bash
terraform plan
```

Apply:

```bash
terraform apply
```

Destroy when finished:

```bash
terraform destroy
```

Always review the Terraform plan before applying or destroying infrastructure.

---

#  AWS Networking Architecture

The project uses a VPC with:

```text
VPC
├── Public Subnet 1
├── Public Subnet 2
├── Public Subnet 3
│
├── Private Subnet 1
├── Private Subnet 2
└── Private Subnet 3
```

The VPC uses:

```text
10.0.0.0/16
```

as the default CIDR.

Public subnet examples:

```text
10.0.1.0/24
10.0.2.0/24
10.0.3.0/24
```

Private subnet examples:

```text
10.0.10.0/24
10.0.20.0/24
10.0.30.0/24
```

The exact values can be changed through Terraform variables.

---

#  Internet Gateway

The Internet Gateway provides internet connectivity for resources in public subnets.

Public route:

```text
0.0.0.0/0
      ↓
Internet Gateway
```

---

#  NAT Gateway

The project uses a single NAT Gateway.

Private subnet traffic follows:

```text
Private Subnet
      ↓
NAT Gateway
      ↓
Internet Gateway
      ↓
Internet
```

A single NAT Gateway is used as a cost-conscious development configuration.

For highly available production environments, NAT gateways are commonly deployed per Availability Zone.

---

#  Security Groups

The EC2 Security Group controls access to the EC2/Jenkins host.

SSH:

```text
TCP 22
```

Jenkins:

```text
TCP 8080
```

Access is controlled using:

```text
allowed_ssh_cidrs
```

The default configuration does not expose these ports to the entire internet.

If access is required, a restricted CIDR such as:

```text
YOUR_PUBLIC_IP/32
```

should be supplied.

---

#  EC2 Infrastructure

Terraform creates an EC2 instance in a public subnet.

The EC2 instance is intended to provide a host for operational tooling such as Jenkins.

The instance uses:

```text
EC2 instance type: t3.medium by default
Root volume: 50 GB gp3
Root volume: encrypted
```

The EC2 bootstrap script installs:

```text
Docker
kubectl
AWS CLI
```

The instance receives a public IP because it is deployed in the public subnet.

---

#  Amazon EKS

The project uses Amazon EKS as the managed Kubernetes control plane.

Terraform creates:

```text
EKS Cluster
       │
       ▼
Managed Node Group
       │
       ├── Worker Node
       └── Worker Node
```

The default managed node group configuration is:

```text
Instance type: t3.medium
Desired nodes: 2
Minimum: 1
Maximum: 4
```

The node group runs inside the private subnets.

---

#  EKS IAM Roles

Two main IAM roles are used.

## EKS Cluster Role

The EKS control plane assumes this role.

It includes:

```text
AmazonEKSClusterPolicy
AmazonEKSVPCResourceController
```

## EKS Node Role

Worker nodes use this role.

It includes policies for:

```text
AmazonEKSWorkerNodePolicy
AmazonEKS_CNI_Policy
AmazonEBSCSIDriverPolicy
```

The EBS CSI permissions are required for Kubernetes persistent storage backed by EBS.

---

#  EKS API Access

The cluster has:

```text
Private API access: enabled
Public API access: enabled
```

Public API access is restricted through:

```text
eks_public_access_cidrs
```

The CIDR should be replaced with the appropriate restricted client network before deployment.

---

#  Kubernetes Architecture

The Kubernetes namespace is:

```text
taskmanager
```

Resources include:

```text
Namespace
StorageClass
PersistentVolumeClaim
PostgreSQL Deployment
PostgreSQL Service
Backend Deployment
Backend Service
Frontend Deployment
Frontend LoadBalancer Service
Ingress
```

---

#  Kubernetes Namespace

The namespace isolates the application resources:

```bash
kubectl get all -n taskmanager
```

Create it manually if needed:

```bash
kubectl apply -f k8s/namespace.yaml
```

---

#  PostgreSQL Deployment

PostgreSQL runs as a Kubernetes Deployment.

Configuration:

```text
Image: postgres:15-alpine
Port: 5432
Replicas: 1
```

The database uses:

```text
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_DB
```

The password comes from a Kubernetes Secret.

The database has:

```text
Readiness Probe
Liveness Probe
CPU requests/limits
Memory requests/limits
Ephemeral storage requests/limits
```

---

#  Persistent Storage

PostgreSQL uses persistent storage.

The storage flow is:

```text
PostgreSQL
    ↓
PersistentVolumeClaim
    ↓
StorageClass
    ↓
AWS EBS CSI Driver
    ↓
Amazon EBS Volume
```

The PVC requests:

```text
5Gi
```

and uses:

```text
ReadWriteOnce
```

---

#  StorageClass

The project defines:

```text
StorageClass: taskmanager-gp3
Provisioner: ebs.csi.aws.com
Volume type: gp3
```

The StorageClass uses:

```text
WaitForFirstConsumer
```

This allows the volume to be provisioned with awareness of where the consuming pod is scheduled.

---

#  Backend Deployment

The backend Deployment runs:

```text
Flask + Gunicorn
```

Port:

```text
8888
```

Default replicas:

```text
1
```

The deployment uses:

```text
RollingUpdate
```

with:

```text
maxUnavailable: 1
maxSurge: 1
```

The backend includes:

### Startup Probe

```text
/api/health
```

### Liveness Probe

```text
/api/health
```

### Readiness Probe

```text
/api/ready
```

These allow Kubernetes to determine whether the backend has started, is healthy, and is ready to receive traffic.

---

#  Frontend Deployment

The frontend runs Nginx.

Port:

```text
80
```

Replicas:

```text
2
```

The frontend includes:

```text
Liveness Probe
Readiness Probe
CPU requests/limits
Memory requests/limits
Ephemeral storage limits
```

---

#  Frontend Service

The frontend Service is:

```text
type: LoadBalancer
```

Therefore AWS can provision an external load balancer for the Kubernetes Service.

Traffic flow:

```text
Internet
   ↓
AWS Load Balancer
   ↓
Frontend Service
   ↓
Frontend Pods
```

---

#  Kubernetes Ingress

An optional Ingress configuration is provided.

Ingress class:

```text
nginx
```

Host:

```text
taskmanager.local
```

Routing:

```text
/
   ↓
frontend:80

/api
   ↓
backend:8888
```

An Nginx Ingress Controller must exist in the cluster for this manifest to actually provide ingress functionality.

The frontend LoadBalancer works independently of this Ingress configuration.

---

#  Kubernetes Deployment Order

A safe deployment sequence is:

```text
1. Namespace
       ↓
2. EBS CSI Driver
       ↓
3. StorageClass
       ↓
4. Kubernetes Secrets
       ↓
5. PostgreSQL PVC
       ↓
6. PostgreSQL Deployment
       ↓
7. Wait for PostgreSQL
       ↓
8. Backend Deployment
       ↓
9. Frontend Deployment
       ↓
10. Ingress
       ↓
11. Verify rollouts
```

---

#  Complete CI/CD Flow

```text
                    GitHub
                       │
                       ▼
                   Jenkins
                       │
               ┌───────┴────────┐
               │                │
               ▼                ▼
        Backend Image     Frontend Image
               │                │
               └───────┬────────┘
                       │
                       ▼
                 Docker Compose
                    Testing
                       │
                       ▼
                  Docker Hub
                       │
                       ▼
                    AWS EKS
                       │
              ┌────────┼─────────┐
              ▼        ▼         ▼
           Frontend Backend PostgreSQL
              │        │         │
              │        │         ▼
              │        │      EBS Volume
              │        │
              └────────┴───────┐
                               ▼
                         Running App
```

---

#  Environment Variables and Secrets

## Local Environment

The repository provides:

```text
.env.example
```

Sensitive values should be stored in:

```text
.env
```

and should not be committed.

Important variables include:

```text
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_DB
SECRET_KEY
FLASK_ENV
DB_HOST
```

---

#  Jenkins Credentials

The Jenkins pipeline expects these credentials:

```text
dockerhub-credentials
aws-credentials
taskmanager-db-password
taskmanager-app-secret-key
```

### Docker Hub

```text
dockerhub-credentials
```

stores Docker Hub username/password.

### AWS

```text
aws-credentials
```

provides AWS credentials to the pipeline.

### PostgreSQL Password

```text
taskmanager-db-password
```

stores the PostgreSQL password.

### Flask Secret

```text
taskmanager-app-secret-key
```

stores the application's secret key.

Credential values are not stored in the Git repository.

---

#  Jenkins Build Parameters

The pipeline uses:

```text
DOCKERHUB_NAMESPACE
AWS_REGION
EKS_CLUSTER_NAME
```

Example:

```text
DOCKERHUB_NAMESPACE = your-dockerhub-username
AWS_REGION = us-east-1
EKS_CLUSTER_NAME = taskmanager-eks
```

These values should be changed according to the deployment environment.

---

#  Security Practices

The project uses several practical security measures.

## Secrets

Sensitive credentials are not hardcoded into the Jenkinsfile.

Jenkins credentials are used instead.

Kubernetes Secrets are generated during deployment.

---

## Password Protection

Application passwords are stored using password hashing rather than storing plaintext passwords.

---

## Kubernetes Service Account Tokens

Application pods disable automatic ServiceAccount token mounting where Kubernetes API access is not required.

This reduces unnecessary credential exposure inside application containers.

---

## EKS API Restrictions

The EKS public API endpoint is restricted through:

```text
eks_public_access_cidrs
```

instead of intentionally allowing every public IP.

---

## EC2 SSH Restrictions

SSH access is controlled using:

```text
allowed_ssh_cidrs
```

The default configuration does not expose SSH globally.

---

## Encrypted EC2 Storage

The EC2 root EBS volume is configured with encryption.

---

## Container Security

The Docker images use relatively small base images:

```text
python:3.11-slim
nginx:alpine
postgres:15-alpine
```

---

#  Health Checks

## Backend

Health:

```text
GET /api/health
```

Readiness:

```text
GET /api/ready
```

These endpoints are used by Kubernetes probes.

---

## PostgreSQL

PostgreSQL uses:

```bash
pg_isready
```

for readiness and liveness checks.

---

## Frontend

The frontend checks:

```text
/
```

through Nginx.

---

#  Deployment Verification

After deploying to EKS:

## Check Cluster

```bash
kubectl cluster-info
```

## Check Nodes

```bash
kubectl get nodes
```

## Check Pods

```bash
kubectl get pods -n taskmanager
```

## Check Services

```bash
kubectl get services -n taskmanager
```

## Check Deployments

```bash
kubectl get deployments -n taskmanager
```

## Check PVC

```bash
kubectl get pvc -n taskmanager
```

## Check Everything

```bash
kubectl get all -n taskmanager
```

---

# 🐛 Troubleshooting Guide

## Issue: Docker Container Does Not Start

Check:

```bash
docker compose ps
```

Then:

```bash
docker compose logs backend
```

or:

```bash
docker compose logs frontend
```

Check the container:

```bash
docker inspect <container>
```

---

# Issue: PostgreSQL Is Not Ready

Check:

```bash
docker compose logs postgres
```

Verify:

```bash
docker compose ps
```

The backend waits for PostgreSQL before starting.

Check environment variables:

```text
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_DB
DB_HOST
```

---

# Issue: Backend Cannot Connect to PostgreSQL

Inside Docker Compose, the backend should use:

```text
DB_HOST=postgres
```

not:

```text
localhost
```

Why?

Because `localhost` inside the backend container refers to the backend container itself.

Docker Compose provides service discovery through the service name:

```text
postgres
```

---

# Issue: Kubernetes Pod Is Pending

Check:

```bash
kubectl get pods -n taskmanager
```

Then:

```bash
kubectl describe pod <pod-name> -n taskmanager
```

Check worker nodes:

```bash
kubectl get nodes
```

Check resources:

```bash
kubectl describe nodes
```

Common causes include:

* insufficient CPU
* insufficient memory
* unavailable node
* PVC not bound
* scheduling constraints

---

# Issue: PostgreSQL PVC Is Pending

Check:

```bash
kubectl get pvc -n taskmanager
```

Then:

```bash
kubectl describe pvc postgres-pvc -n taskmanager
```

Check StorageClass:

```bash
kubectl get storageclass
```

Check EBS CSI:

```bash
aws eks describe-addon \
  --cluster-name taskmanager-eks \
  --addon-name aws-ebs-csi-driver
```

The EBS CSI add-on must be available for EBS-backed persistent storage.

---

# Issue: Backend Pod Is Not Ready

Check:

```bash
kubectl get pods -n taskmanager
```

Then:

```bash
kubectl describe pod <backend-pod> -n taskmanager
```

View logs:

```bash
kubectl logs <backend-pod> -n taskmanager
```

Check the health endpoint:

```text
/api/health
```

and readiness endpoint:

```text
/api/ready
```

---

# Issue: Frontend Is Not Accessible

Check:

```bash
kubectl get service frontend -n taskmanager
```

The frontend Service should be:

```text
LoadBalancer
```

Check:

```bash
kubectl describe service frontend -n taskmanager
```

Check frontend pods:

```bash
kubectl get pods -l app=frontend -n taskmanager
```

---

# Issue: Jenkins Cannot Access EKS

Verify AWS credentials:

```bash
aws sts get-caller-identity
```

Verify the cluster:

```bash
aws eks describe-cluster \
  --name taskmanager-eks \
  --region us-east-1
```

Then configure kubeconfig:

```bash
aws eks update-kubeconfig \
  --name taskmanager-eks \
  --region us-east-1
```

Test:

```bash
kubectl get nodes
```

---

# Issue: Jenkins Docker Build Fails

Check:

```bash
docker version
```

Check:

```bash
docker info
```

Check Dockerfile:

```text
backend/Dockerfile
frontend/Dockerfile
```

Build manually:

```bash
docker build -t taskmanager-backend:test backend
```

and:

```bash
docker build -t taskmanager-frontend:test frontend
```

---

# Issue: Docker Hub Push Fails

Verify Docker login:

```bash
docker login
```

Check the image:

```bash
docker images
```

Verify the image name:

```text
<DOCKERHUB_NAMESPACE>/taskmanager-backend:<BUILD_NUMBER>
```

---

# Issue: Kubernetes Deployment Rollout Fails

Check:

```bash
kubectl rollout status deployment/backend \
  -n taskmanager
```

Then:

```bash
kubectl describe deployment backend \
  -n taskmanager
```

Check pods:

```bash
kubectl get pods -n taskmanager
```

View logs:

```bash
kubectl logs deployment/backend \
  -n taskmanager
```

---

#  Important Commands

## Git

```bash
git status
git add .
git commit -m "message"
git push origin main
git log --oneline
```

---

#  Docker

Build:

```bash
docker build -t taskmanager-backend ./backend
```

List images:

```bash
docker images
```

List containers:

```bash
docker ps
```

View logs:

```bash
docker logs <container>
```

Remove container:

```bash
docker rm <container>
```

---

#  Docker Compose

Start:

```bash
docker compose up --build
```

Background:

```bash
docker compose up -d
```

Check:

```bash
docker compose ps
```

Logs:

```bash
docker compose logs -f
```

Stop:

```bash
docker compose down
```

Remove database volume:

```bash
docker compose down -v
```

---

#  Terraform Commands

```bash
terraform init
terraform fmt
terraform validate
terraform plan
terraform apply
terraform output
terraform destroy
```

Useful debugging:

```bash
terraform show
terraform state list
```

---

#  AWS CLI Commands

Check identity:

```bash
aws sts get-caller-identity
```

Check EKS:

```bash
aws eks list-clusters
```

Update kubeconfig:

```bash
aws eks update-kubeconfig \
  --name taskmanager-eks \
  --region us-east-1
```

Check EBS CSI:

```bash
aws eks describe-addon \
  --cluster-name taskmanager-eks \
  --addon-name aws-ebs-csi-driver \
  --region us-east-1
```

---

#  Kubernetes Commands

Cluster:

```bash
kubectl cluster-info
kubectl get nodes
```

Pods:

```bash
kubectl get pods -n taskmanager
kubectl get pods -n taskmanager -o wide
```

Deployments:

```bash
kubectl get deployments -n taskmanager
```

Services:

```bash
kubectl get services -n taskmanager
```

PVC:

```bash
kubectl get pvc -n taskmanager
```

StorageClass:

```bash
kubectl get storageclass
```

Logs:

```bash
kubectl logs <pod> -n taskmanager
```

Describe:

```bash
kubectl describe pod <pod> -n taskmanager
```

Rollout:

```bash
kubectl rollout status deployment/backend -n taskmanager
```

Restart:

```bash
kubectl rollout restart deployment/backend -n taskmanager
```

---

#  Updating the Application

The normal workflow is:

```text
1. Modify application code
        ↓
2. Test locally
        ↓
3. Commit changes
        ↓
4. Push to GitHub
        ↓
5. Jenkins starts
        ↓
6. Build new Docker images
        ↓
7. Run Compose test
        ↓
8. Push new build-tagged images
        ↓
9. Configure EKS
        ↓
10. Apply Kubernetes configuration
        ↓
11. Update deployment images
        ↓
12. Wait for rollout
        ↓
13. Verify application
```

---

#  Destroying the Infrastructure

For disposable development environments:

```bash
cd terraform
terraform plan -destroy
terraform destroy
```

Always review what will be deleted.

AWS resources such as:

```text
EC2
EKS
NAT Gateway
Load Balancer
EBS
```

can incur charges.

Persistent resources should be reviewed carefully before destruction.

---

#  Project Limitations

This project intentionally focuses on core DevOps and cloud deployment concepts.

The current implementation does **not** include:

* SonarQube
* Prometheus
* Grafana
* AlertManager
* ArgoCD
* Helm
* Redis
* Kafka
* Loki
* Service mesh
* AWS RDS
* AWS ECR
* Automated rollback
* Full production-grade observability platform
* Multi-region deployment

These are not required for the current project workflow.

---

#  Future Improvements

Possible future improvements include:

### CI/CD

* Automated rollback
* Approval gates
* More extensive automated tests
* Security scanning
* Image vulnerability scanning

### Kubernetes

* Horizontal Pod Autoscaler
* PodDisruptionBudget
* NetworkPolicies
* More replicas for backend
* Separate production/staging namespaces

### Observability

* Prometheus
* Grafana
* Centralized logging
* Alerting

### Infrastructure

* S3 remote Terraform state
* Terraform state locking
* Highly available NAT gateways
* Private EKS API endpoint
* More restrictive IAM policies

### Application

* Automated database migrations
* More comprehensive tests
* API documentation
* Better error handling

These are future improvements rather than claims about the current implementation.

---

#  Current Architecture vs Production Architecture

The current project is designed as a practical DevOps portfolio project.

```text
CURRENT PROJECT

GitHub
   ↓
Jenkins
   ↓
Docker
   ↓
Docker Hub
   ↓
AWS EKS
   ↓
Kubernetes
   ├── Frontend
   ├── Backend
   └── PostgreSQL
          ↓
        EBS
```

A larger production environment could additionally introduce:

```text
Production Extensions

        GitHub
           ↓
        CI/CD
           ↓
    Image Security Scan
           ↓
     Container Registry
           ↓
        EKS
      /     \
Frontend   Backend
              │
              ▼
        Managed Database

Observability:
Prometheus → Grafana → Alerting

GitOps:
ArgoCD

Security:
Secrets Manager / External Secrets
```

These additional components are possible future extensions and are not part of the current implementation.

---

#  Project Documentation

The repository contains additional documentation for understanding the implementation.

### `DEVOPS-FILES-EXPLAINED.md`

Provides explanations of the DevOps-related files and their purpose.

### `INTERVIEW-PROJECT-EXPLANATION.md`

Provides a deeper explanation of the project for interview preparation.

### `PROJECT-QUESTION-BANK.md`

Contains project-specific interview questions and answers.

### `terraform/README.md`

Contains Terraform-specific infrastructure setup instructions.

---

#  Contributing

## Development Workflow

Create a feature branch:

```bash
git checkout -b feature/my-feature
```

Make your changes.

Test locally:

```bash
docker compose up --build
```

Check the application.

Then commit:

```bash
git add .
git commit -m "feat: describe change"
```

Push:

```bash
git push origin feature/my-feature
```

Create a Pull Request.

---

#  Project Summary

| Category               | Implementation         |
| ---------------------- | ---------------------- |
| Application            | Task Manager           |
| Backend                | Flask                  |
| Frontend               | HTML/CSS/JavaScript    |
| Web Server             | Nginx                  |
| Application Server     | Gunicorn               |
| Database               | PostgreSQL 15          |
| Local Containerization | Docker                 |
| Local Orchestration    | Docker Compose         |
| Cloud                  | AWS                    |
| Infrastructure as Code | Terraform              |
| Kubernetes             | Kubernetes             |
| Managed Kubernetes     | Amazon EKS             |
| Worker Nodes           | EKS Managed Node Group |
| Container Registry     | Docker Hub             |
| CI/CD                  | Jenkins                |
| Persistent Storage     | Amazon EBS             |
| Storage Driver         | AWS EBS CSI            |
| Database Storage       | 5Gi PVC                |
| Frontend Port          | 80                     |
| Backend Port           | 8888                   |
| PostgreSQL Port        | 5432                   |
| Kubernetes Namespace   | taskmanager            |

---

#  30-Second Interview Explanation

> "I built a cloud-native Task Manager application using Flask, PostgreSQL and a static Nginx frontend. I containerized the application using Docker and Docker Compose for local testing. For cloud deployment, I used Terraform to provision AWS networking, EC2, IAM and an EKS cluster with managed worker nodes. I deployed the frontend, Flask backend and PostgreSQL database using Kubernetes, with persistent EBS-backed storage for PostgreSQL. Finally, I implemented a Jenkins CI/CD pipeline that builds the Docker images, tests the application using Docker Compose, pushes the images to Docker Hub, and deploys the updated images to EKS."

---

#  2-Minute Interview Explanation

> "The project is a full-stack Task Manager application with a Flask backend, Nginx frontend and PostgreSQL database. I first containerized the three services using Docker. Docker Compose allows me to run the complete application locally and verify that the backend can communicate with PostgreSQL before deploying it to AWS.
>
> For the cloud infrastructure, I used Terraform. Terraform creates a VPC with public and private subnets across multiple Availability Zones, an Internet Gateway, NAT Gateway, route tables and security groups. It also provisions an EC2 instance and an Amazon EKS cluster with a managed node group running in the private subnets.
>
> On Kubernetes, I created a dedicated namespace for the application. PostgreSQL runs with a PersistentVolumeClaim backed by Amazon EBS through the AWS EBS CSI driver. The Flask backend runs as a Deployment with health probes and resource limits, while the Nginx frontend runs with two replicas and is exposed using a LoadBalancer Service.
>
> For CI/CD, Jenkins checks out the code, builds the frontend and backend Docker images, starts the application using Docker Compose for a basic integration check, pushes build-number-tagged images to Docker Hub, configures access to EKS, applies the Kubernetes resources, updates the images and waits for the deployments to successfully roll out.
>
> The main goal of the project is to demonstrate the complete path from source code to containerization, infrastructure provisioning, Kubernetes deployment and CI/CD automation."

---

#  Final Project Flow

```text
                     ┌───────────────┐
                     │   Developer   │
                     └───────┬───────┘
                             │
                             ▼
                     ┌───────────────┐
                     │    GitHub     │
                     └───────┬───────┘
                             │
                             ▼
                     ┌───────────────┐
                     │    Jenkins    │
                     └───────┬───────┘
                             │
             ┌───────────────┼────────────────┐
             │               │                │
             ▼               ▼                ▼
        Docker Build    Compose Test     Docker Hub
             │                                │
             └───────────────┬────────────────┘
                             │
                             ▼
                    ┌────────────────┐
                    │    AWS EKS     │
                    │   Kubernetes   │
                    └───────┬────────┘
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
        Frontend         Backend       PostgreSQL
         Nginx            Flask          Database
          :80             :8888           :5432
             │              │              │
             │              │              ▼
             │              │         EBS Storage
             │              │
             └──────────────┴──────────────┐
                                           ▼
                                      Task Manager
```

---

#  Important Note

This README documents the **current implementation of the repository**.

It deliberately does not claim that the project contains monitoring, GitOps, ECR, RDS, Helm, SonarQube, Prometheus/Grafana, automatic rollback, or other components that are not part of the current implementation.

The goal is to keep the documentation comprehensive while keeping the architecture technically accurate.
