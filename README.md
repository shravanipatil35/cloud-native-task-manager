# Cloud-Native Task Manager – Complete DevOps Platform

A full-stack task management application deployed using modern DevOps and cloud-native practices.

This project demonstrates the complete flow from application development to containerization, infrastructure provisioning, Kubernetes deployment, and CI/CD automation using Jenkins.

The main focus of the project is to understand and demonstrate practical DevOps concepts such as:

* Docker containerization
* Docker Compose
* Terraform Infrastructure as Code
* AWS VPC and networking
* Amazon EKS
* Kubernetes deployments and services
* Persistent storage using EBS CSI
* Jenkins CI/CD
* Docker Hub image publishing
* Kubernetes-based application deployment
* Environment variables and secret management
* Health checks and rolling deployments

---

# Table of Contents

* [Project Overview](#project-overview)
* [Architecture](#architecture)
* [Architecture Components](#architecture-components)
* [Technology Stack](#technology-stack)
* [Application Overview](#application-overview)
* [Complete Project Workflow](#complete-project-workflow)
* [Repository Structure](#repository-structure)
* [Prerequisites](#prerequisites)
* [Run Application Locally](#run-application-locally)
* [Docker Architecture](#docker-architecture)
* [AWS Infrastructure with Terraform](#aws-infrastructure-with-terraform)
* [AWS Network Architecture](#aws-network-architecture)
* [EC2 Instance](#ec2-instance)
* [Amazon EKS](#amazon-eks)
* [Kubernetes Architecture](#kubernetes-architecture)
* [PostgreSQL Persistent Storage](#postgresql-persistent-storage)
* [Frontend and Backend Deployment](#frontend-and-backend-deployment)
* [Kubernetes Services](#kubernetes-services)
* [Ingress](#ingress)
* [Jenkins CI/CD Pipeline](#jenkins-cicd-pipeline)
* [Jenkins Pipeline Stages](#jenkins-pipeline-stages)
* [Jenkins Credentials](#jenkins-credentials)
* [Environment Variables](#environment-variables)
* [Security Practices](#security-practices)
* [Health Checks](#health-checks)
* [Deployment Verification](#deployment-verification)
* [Troubleshooting](#troubleshooting)
* [Important Commands](#important-commands)
* [Updating the Application](#updating-the-application)
* [Destroying AWS Infrastructure](#destroying-aws-infrastructure)
* [Current Project Scope](#current-project-scope)
* [Limitations](#limitations)
* [Future Improvements](#future-improvements)
* [Current vs Production Architecture](#current-vs-production-architecture)
* [Project Documentation](#project-documentation)
* [Contributing](#contributing)
* [Interview Explanation](#interview-explanation)
* [Summary](#summary)

---

# Project Overview

Cloud-Native Task Manager is a task management application consisting of:

* Flask backend
* PostgreSQL database
* Static frontend served using Nginx
* Docker containers
* Docker Compose for local development
* Terraform for AWS infrastructure
* Kubernetes manifests for application deployment
* Amazon EKS for Kubernetes orchestration
* Jenkins for CI/CD automation
* Docker Hub for container image storage

The project is designed as a practical DevOps project where the application is kept relatively simple while the main focus remains on infrastructure, containerization, Kubernetes, and CI/CD.

---

# Architecture

```text
                         Developer
                             |
                             |
                         Git Push
                             |
                             v
                     +----------------+
                     |    GitHub      |
                     +----------------+
                             |
                             |
                             v
                     +----------------+
                     |    Jenkins     |
                     |    CI/CD       |
                     +----------------+
                             |
              +--------------+--------------+
              |                             |
              v                             v
       Docker Build                  Docker Compose Test
              |
              v
       +---------------+
       |   Docker Hub  |
       +---------------+
              |
              |
              v
       +-----------------------+
       |      AWS / EKS        |
       |                       |
       |  +-----------------+  |
       |  | Kubernetes      |  |
       |  | Namespace       |  |
       |  |                 |  |
       |  | Frontend        |  |
       |  | Backend         |  |
       |  | PostgreSQL      |  |
       |  +-----------------+  |
       |                       |
       +-----------------------+
              |
              v
        Application Users
```

---

# Architecture Components

| Component          | Purpose                                  |
| ------------------ | ---------------------------------------- |
| GitHub             | Source code repository                   |
| Flask              | Backend API                              |
| PostgreSQL         | Application database                     |
| Nginx              | Serves frontend and proxies API requests |
| Docker             | Application containerization             |
| Docker Compose     | Local multi-container environment        |
| Terraform          | AWS infrastructure provisioning          |
| AWS VPC            | Network isolation                        |
| EC2                | General operational host                 |
| Amazon EKS         | Managed Kubernetes cluster               |
| Kubernetes         | Application orchestration                |
| EBS CSI Driver     | Persistent EBS storage for PostgreSQL    |
| Docker Hub         | Container image registry                 |
| Jenkins            | CI/CD automation                         |
| Kubernetes Secrets | Runtime secret configuration             |

---

# Technology Stack

## Application

* Python
* Flask
* Flask-SQLAlchemy
* PostgreSQL
* HTML
* CSS
* JavaScript

## Containerization

* Docker
* Docker Compose
* Gunicorn
* Nginx

## Infrastructure

* AWS
* Terraform
* VPC
* Internet Gateway
* NAT Gateway
* Route Tables
* Security Groups
* EC2
* IAM
* Amazon EKS
* EBS

## Kubernetes

* Kubernetes
* Deployments
* Services
* Namespace
* PersistentVolumeClaim
* StorageClass
* Secrets
* Health probes
* Resource requests and limits
* Rolling updates
* LoadBalancer Service
* Optional Nginx Ingress

## CI/CD

* Jenkins
* Docker Hub
* AWS CLI
* kubectl
* Docker Compose

---

# Application Overview

The application is a task management system.

Users can manage tasks through the web application.

The application consists of:

```text
Frontend
   |
   | HTTP
   v
Nginx
   |
   | /api/
   v
Flask Backend
   |
   | SQL
   v
PostgreSQL
```

The backend provides API endpoints for application functionality and health checking.

The frontend is served as static content through Nginx.

Nginx also proxies API requests to the Flask backend.

---

# Complete Project Workflow

The complete DevOps workflow is:

```text
1. Developer changes application code
              |
              v
2. Push code to GitHub
              |
              v
3. Jenkins starts pipeline
              |
              v
4. Build backend Docker image
              |
              v
5. Build frontend Docker image
              |
              v
6. Start application using Docker Compose
              |
              v
7. Run basic health checks
              |
              v
8. Push images to Docker Hub
              |
              v
9. Configure AWS EKS access
              |
              v
10. Ensure EBS CSI add-on is available
              |
              v
11. Create/update Kubernetes Secrets
              |
              v
12. Deploy PostgreSQL
              |
              v
13. Wait for PostgreSQL rollout
              |
              v
14. Deploy backend and frontend
              |
              v
15. Update deployments with new image tags
              |
              v
16. Wait for Kubernetes rollouts
              |
              v
17. Verify pods and services
```

---

# Repository Structure

```text
cloud-native-task-manager/
│
├── backend/
│   ├── app/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── run.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── wait-for-db.sh
│   └── .dockerignore
│
├── frontend/
│   ├── css/
│   ├── js/
│   ├── html files
│   ├── Dockerfile
│   ├── nginx.conf
│   └── .dockerignore
│
├── k8s/
│   ├── namespace.yaml
│   ├── postgres-deployment.yaml
│   ├── postgres-pvc.yaml
│   ├── storage-class.yaml
│   ├── backend-deployment.yaml
│   ├── frontend-deployment.yaml
│   ├── ingress.yaml
│   └── load-generator.yaml
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
│   └── .terraform.lock.hcl
│
├── jenkins/
│   └── jenkins-deployment.yaml
│
├── docker-compose.yml
├── Jenkinsfile
├── .env.example
├── .gitignore
├── .dockerignore
├── DEVOPS-FILES-EXPLAINED.md
├── INTERVIEW-PROJECT-EXPLANATION.md
├── PROJECT-QUESTION-BANK.md
└── README.md
```

---

# Prerequisites

Before running the complete project, install:

## Local Development

* Git
* Docker
* Docker Compose
* Python
* Node.js if required for frontend development

## AWS

* AWS account
* AWS CLI
* Configured AWS credentials
* IAM permissions for required AWS resources

## Infrastructure

* Terraform
* kubectl

## CI/CD

* Jenkins
* Docker Hub account
* Jenkins Docker support
* Jenkins AWS credentials
* Jenkins Kubernetes deployment access

---

# Run Application Locally

The easiest way to run the complete application locally is Docker Compose.

## Clone Repository

```bash
git clone <repository-url>
cd cloud-native-task-manager
```

## Configure Environment

Copy the example environment file:

```bash
cp .env.example .env
```

Update the values according to your local environment.

Do not commit `.env` files containing real credentials.

---

# Start with Docker Compose

Run:

```bash
docker compose up --build
```

This starts:

```text
PostgreSQL
    |
    v
Backend
    |
    v
Frontend / Nginx
```

The frontend is available on:

```text
http://localhost
```

The backend runs on:

```text
http://localhost:8888
```

Backend health endpoint:

```text
http://localhost:8888/api/health
```

Stop the application:

```bash
docker compose down
```

Remove containers and database volume:

```bash
docker compose down --volumes
```

---

# Docker Architecture

The application uses three main containers locally.

```text
+-----------------------+
|      PostgreSQL       |
|       Port 5432       |
+-----------+-----------+
            |
            |
+-----------v-----------+
|    Flask Backend      |
|       Port 8888       |
|       Gunicorn        |
+-----------+-----------+
            |
            |
+-----------v-----------+
|     Nginx Frontend    |
|        Port 80        |
+-----------------------+
```

## Backend Container

The backend Docker image is based on:

```text
python:3.11-slim
```

The application is served using Gunicorn.

The backend container waits for PostgreSQL to become available before starting the application.

## Frontend Container

The frontend uses:

```text
nginx:alpine
```

Nginx:

* Serves frontend files
* Handles frontend routes
* Proxies `/api/` requests to the backend

---

# AWS Infrastructure with Terraform

Terraform is used to provision the AWS infrastructure.

The infrastructure includes:

* VPC
* Public subnets
* Private subnets
* Internet Gateway
* NAT Gateway
* Route tables
* Security groups
* EC2 instance
* IAM roles
* Amazon EKS cluster
* EKS managed node group

---

# Terraform Configuration

Navigate to the Terraform directory:

```bash
cd terraform
```

Initialize Terraform:

```bash
terraform init
```

Create your configuration file:

```bash
cp terraform.tfvars.example terraform.tfvars
```

Update:

* AWS region
* EC2 AMI ID
* EKS version
* Availability Zones
* EKS public API CIDR
* SSH public key
* allowed SSH CIDRs if required

---

# Terraform Validation

Format Terraform files:

```bash
terraform fmt -recursive
```

Validate configuration:

```bash
terraform validate
```

Review infrastructure changes:

```bash
terraform plan
```

Apply infrastructure:

```bash
terraform apply
```

Terraform creates the AWS infrastructure required for the Kubernetes deployment.

---

# AWS Network Architecture

The VPC uses:

```text
VPC
10.0.0.0/16
│
├── Public Subnets
│   ├── Public Subnet 1
│   ├── Public Subnet 2
│   └── Public Subnet 3
│
├── Private Subnets
│   ├── Private Subnet 1
│   ├── Private Subnet 2
│   └── Private Subnet 3
│
├── Internet Gateway
│
└── NAT Gateway
```

The public subnets provide internet-facing connectivity.

The private subnets are used for EKS worker nodes.

The NAT Gateway allows resources in private subnets to access the internet for outbound communication without requiring public IP addresses.

---

# Security Groups

The EC2 security group controls access to the operational host.

SSH access is configurable using:

```text
allowed_ssh_cidrs
```

By default, this list is empty.

This prevents accidentally exposing SSH access before an administrator explicitly configures an allowed CIDR.

The security group allows outbound traffic.

---

# EC2 Instance

Terraform provisions an EC2 instance in a public subnet.

The instance is configured with:

* Docker
* kubectl
* AWS CLI

The EC2 instance is intended as a general operational host.

It is not required to run the Jenkins controller.

Jenkins can optionally be deployed inside Kubernetes using the provided Jenkins Kubernetes manifest.

The EC2 instance receives a public IP because it is deployed in a public subnet with public IP association enabled.

---

# Amazon EKS

The project uses Amazon EKS as the Kubernetes control plane.

The EKS cluster contains a managed node group.

Default configuration includes:

```text
Desired nodes: 2
Minimum nodes: 1
Maximum nodes: 4
Instance type: t3.medium
```

The managed node group runs in private subnets.

---

# EKS IAM Roles

Terraform creates IAM roles for:

## EKS Cluster

The EKS cluster role provides permissions required by the EKS control plane.

## EKS Worker Nodes

Worker nodes use an IAM role with permissions including:

* AmazonEKSWorkerNodePolicy
* AmazonEKS_CNI_Policy
* AmazonEBSCSIDriverPolicy

These permissions allow the worker nodes and storage components to operate correctly.

---

# EKS API Access

The Kubernetes API endpoint is configured with:

```text
Private access: enabled
Public access: enabled
```

Public access is restricted using:

```text
eks_public_access_cidrs
```

The CIDR should be replaced with the administrator's required public IP or network range.

Do not use unrestricted public access for a real production environment unless there is a specific security reason.

---

# Kubernetes Architecture

The Kubernetes deployment uses a dedicated namespace:

```text
taskmanager
```

The application architecture is:

```text
                 LoadBalancer
                      |
                      v
               +-------------+
               |  Frontend   |
               |  Nginx      |
               +------+------+
                      |
                    /api
                      |
                      v
               +-------------+
               |   Backend   |
               |    Flask    |
               +------+------+
                      |
                      v
               +-------------+
               | PostgreSQL  |
               +------+------+
                      |
                      v
               EBS Persistent Storage
```

---

# Kubernetes Resources

The project uses the following Kubernetes resources:

* Namespace
* Deployments
* Services
* PersistentVolumeClaim
* StorageClass
* Secrets
* Health probes
* Resource requests and limits
* Optional Ingress

---

# Namespace

All application resources are deployed into:

```text
taskmanager
```

Create the namespace manually:

```bash
kubectl apply -f k8s/namespace.yaml
```

Check:

```bash
kubectl get namespace
```

---

# PostgreSQL Persistent Storage

PostgreSQL uses persistent storage.

The project defines a:

```text
StorageClass
```

using:

```text
EBS CSI Driver
```

The storage class uses:

```text
gp3
```

and:

```text
WaitForFirstConsumer
```

This allows Kubernetes to provision the EBS volume in a suitable Availability Zone when the PostgreSQL pod is scheduled.

---

# PostgreSQL PVC

The PostgreSQL PersistentVolumeClaim requests:

```text
5Gi
```

with:

```text
ReadWriteOnce
```

The PVC is mounted by the PostgreSQL pod.

This prevents database data from being stored only inside the container filesystem.

---

# PostgreSQL Deployment

The project uses:

```text
postgres:15-alpine
```

PostgreSQL runs as a single replica.

The database has:

* Persistent storage
* Database password from Kubernetes Secret
* Readiness probe
* Liveness probe
* Resource requests
* Resource limits

---

# Backend Deployment

The backend runs as a Kubernetes Deployment.

Default configuration:

```text
Replicas: 1
Port: 8888
```

The backend uses:

```text
Gunicorn
```

for serving the Flask application.

Environment configuration includes:

```text
FLASK_ENV
DATABASE_HOST
DATABASE_NAME
DATABASE_USER
DATABASE_PASSWORD
SECRET_KEY
```

Sensitive values are supplied through Kubernetes Secrets.

The backend also has:

* Startup probe
* Readiness probe
* Liveness probe
* Resource requests
* Resource limits
* Rolling update configuration

---

# Frontend Deployment

The frontend runs using Nginx.

Default configuration:

```text
Replicas: 2
Port: 80
```

The frontend deployment includes:

* Readiness probe
* Liveness probe
* Resource requests
* Resource limits
* Rolling update configuration

Two replicas provide basic availability during rolling deployments.

---

# Kubernetes Services

The project uses three main services.

## Frontend Service

Type:

```text
LoadBalancer
```

Port:

```text
80
```

This provides external access to the frontend through the AWS load balancer created by Kubernetes.

## Backend Service

Type:

```text
ClusterIP
```

Port:

```text
8888
```

The backend is intended to be accessed internally by other Kubernetes resources.

## PostgreSQL Service

Type:

```text
ClusterIP
```

Port:

```text
5432
```

The backend communicates with PostgreSQL through the Kubernetes service.

---

# Ingress

The project also includes an optional Nginx Ingress configuration.

The configured hostname is:

```text
taskmanager.local
```

Routes include:

```text
/
```

to the frontend service.

And:

```text
/api
```

to the backend service.

The Ingress manifest is optional and requires an Nginx Ingress Controller to already exist in the cluster.

The default frontend `LoadBalancer` service can be used without the optional Ingress controller.

---

# Kubernetes Deployment Order

A typical deployment order is:

```text
1. Namespace
       |
       v
2. StorageClass
       |
       v
3. Kubernetes Secrets
       |
       v
4. PostgreSQL PVC
       |
       v
5. PostgreSQL Deployment
       |
       v
6. Backend Deployment
       |
       v
7. Frontend Deployment
       |
       v
8. Services
       |
       v
9. Optional Ingress
```

The Jenkins pipeline automates the required deployment sequence.

---

# Jenkins CI/CD Pipeline

The project uses Jenkins for CI/CD.

The Jenkins pipeline performs:

```text
Checkout
   |
   v
Build Docker Images
   |
   v
Docker Compose Integration Test
   |
   v
Push Images to Docker Hub
   |
   v
Deploy to Amazon EKS
```

---

# Jenkins Pipeline Stages

## Stage 1 – Checkout

Jenkins checks out the source code from GitHub.

---

## Stage 2 – Build Images

Jenkins builds:

```text
Backend Docker Image
Frontend Docker Image
```

Images are tagged using the Jenkins build number.

Example:

```text
username/taskmanager-backend:15
username/taskmanager-frontend:15
```

Using the Jenkins build number gives every pipeline build a unique image tag.

---

# Stage 3 – Test with Docker Compose

Jenkins starts the application using Docker Compose.

The pipeline:

1. Starts PostgreSQL
2. Starts backend
3. Starts frontend
4. Waits for the backend
5. Checks the backend health endpoint
6. Checks the frontend
7. Cleans up the containers

Backend health endpoint:

```text
/api/health
```

This provides a basic integration/smoke test before pushing the images.

---

# Stage 4 – Push Images

After successful testing, Jenkins authenticates with Docker Hub.

The backend and frontend images are pushed using the Jenkins build number.

Example:

```text
DOCKERHUB_NAMESPACE/taskmanager-backend:BUILD_NUMBER
DOCKERHUB_NAMESPACE/taskmanager-frontend:BUILD_NUMBER
```

---

# Stage 5 – Deploy to EKS

Jenkins uses AWS credentials to configure access to EKS.

The pipeline runs:

```bash
aws eks update-kubeconfig
```

It then:

1. Applies the Kubernetes namespace
2. Checks for the EBS CSI add-on
3. Creates it if required
4. Waits for the add-on to become active
5. Applies the StorageClass
6. Creates/updates Kubernetes Secrets
7. Deploys PostgreSQL
8. Waits for PostgreSQL
9. Deploys backend
10. Deploys frontend
11. Updates backend image
12. Updates frontend image
13. Waits for rollouts
14. Displays pods and services

---

# Jenkins Image Deployment

The Kubernetes deployment initially contains baseline image references.

Jenkins updates the running deployment using:

```bash
kubectl set image
```

For example:

```bash
kubectl set image deployment/taskmanager-backend \
backend=DOCKERHUB_NAMESPACE/taskmanager-backend:BUILD_NUMBER
```

This allows each Jenkins build to deploy a specific image version.

---

# Jenkins Credentials

The Jenkins pipeline expects credentials with the following IDs:

```text
dockerhub-credentials
aws-credentials
taskmanager-db-password
taskmanager-app-secret-key
```

## dockerhub-credentials

Used for authenticating with Docker Hub.

## aws-credentials

Used by Jenkins to access AWS and configure EKS access.

## taskmanager-db-password

Used to configure the PostgreSQL database password.

## taskmanager-app-secret-key

Used as the Flask application secret key.

Credentials should be stored in Jenkins Credentials Manager rather than directly inside the Jenkinsfile.

---

# Jenkins Build Parameters

The pipeline supports parameters including:

```text
DOCKERHUB_NAMESPACE
AWS_REGION
EKS_CLUSTER_NAME
```

Example defaults include:

```text
AWS_REGION=us-east-1
EKS_CLUSTER_NAME=taskmanager-eks
```

These values can be changed through Jenkins build parameters.

---

# Optional Jenkins Deployment Inside Kubernetes

The repository includes an optional Jenkins deployment manifest.

The Jenkins controller:

* Runs inside Kubernetes
* Uses a persistent volume
* Uses a ClusterIP service
* Does not expose Jenkins directly through a public LoadBalancer
* Does not automatically mount a Kubernetes service-account token

The Jenkins deployment uses the project's EBS-backed storage class.

Before deploying Jenkins, the EBS CSI driver must be available.

To access Jenkins locally through port forwarding:

```bash
kubectl port-forward -n jenkins svc/jenkins 8080:8080
```

Then access Jenkins through:

```text
localhost:8080
```

This Jenkins deployment is optional. Jenkins can also be hosted separately.

---

# Environment Variables

The project avoids placing application secrets directly in source code.

Common configuration values include:

```text
POSTGRES_USER
POSTGRES_DB
POSTGRES_PASSWORD
DATABASE_HOST
DATABASE_PORT
DATABASE_NAME
DATABASE_USER
DATABASE_PASSWORD
SECRET_KEY
```

For local development, configuration can be supplied through `.env`.

For Kubernetes deployment, sensitive values are supplied through Kubernetes Secrets.

---

# Kubernetes Secrets

The Jenkins pipeline creates or updates Kubernetes Secrets during deployment.

Secrets are used for values such as:

```text
Database password
Application secret key
```

This prevents passwords and secret keys from being hardcoded directly inside deployment manifests.

---

# Security Practices

The project includes several basic security practices.

## Secrets

Sensitive values are not committed directly into the repository.

Example configuration files use placeholders.

---

## Kubernetes Service Account Tokens

Application pods disable automatic service-account-token mounting where it is not required.

Example:

```yaml
automountServiceAccountToken: false
```

This follows the principle of reducing unnecessary Kubernetes API access.

---

## EKS API Access

The EKS public API endpoint is restricted using configurable CIDRs.

The example configuration contains a documentation placeholder that must be replaced with the administrator's actual IP or network range.

---

## Security Groups

SSH access to the EC2 instance is controlled using:

```text
allowed_ssh_cidrs
```

The default value is empty.

---

## Container Images

The Docker images use lightweight base images:

```text
python:3.11-slim
nginx:alpine
postgres:15-alpine
```

The project keeps the Dockerfiles simple and focused on the application's actual requirements.

---

# Health Checks

Health checks are used at multiple levels.

## Backend

The backend provides:

```text
/api/health
```

and:

```text
/api/ready
```

These endpoints are used by Kubernetes probes.

---

## PostgreSQL

PostgreSQL uses:

```text
pg_isready
```

for readiness and liveness checks.

---

## Frontend

The frontend uses the Nginx root endpoint for readiness and liveness checks.

---

# Kubernetes Resource Management

The application deployments define Kubernetes resource requests and limits.

Example concept:

```text
Requests
   |
   +-- CPU
   +-- Memory

Limits
   |
   +-- CPU
   +-- Memory
```

This helps Kubernetes schedule workloads and prevents individual containers from consuming unlimited resources.

---

# Rolling Updates

Backend and frontend deployments use Kubernetes rolling update strategies.

The goal is to replace old pods gradually rather than deleting all application pods at once.

The deployment strategy uses:

```text
maxUnavailable
maxSurge
```

This provides basic zero-downtime-style deployment behavior for the application layer.

---

# Deployment Verification

After deployment:

```bash
kubectl get pods -n taskmanager
```

Check services:

```bash
kubectl get svc -n taskmanager
```

Check deployments:

```bash
kubectl get deployments -n taskmanager
```

Check PVC:

```bash
kubectl get pvc -n taskmanager
```

Check StorageClass:

```bash
kubectl get storageclass
```

Check pod details:

```bash
kubectl describe pod <pod-name> -n taskmanager
```

Check logs:

```bash
kubectl logs <pod-name> -n taskmanager
```

---

# Important Kubernetes Commands

## Cluster Information

```bash
kubectl cluster-info
```

```bash
kubectl get nodes
```

---

## Pods

```bash
kubectl get pods -n taskmanager
```

```bash
kubectl get pods -n taskmanager -o wide
```

---

## Deployments

```bash
kubectl get deployments -n taskmanager
```

```bash
kubectl rollout status deployment/taskmanager-backend -n taskmanager
```

```bash
kubectl rollout status deployment/taskmanager-frontend -n taskmanager
```

---

## Services

```bash
kubectl get svc -n taskmanager
```

---

## Logs

```bash
kubectl logs deployment/taskmanager-backend -n taskmanager
```

```bash
kubectl logs deployment/taskmanager-frontend -n taskmanager
```

---

## Describe Resources

```bash
kubectl describe pod <pod-name> -n taskmanager
```

```bash
kubectl describe deployment taskmanager-backend -n taskmanager
```

---

## Storage

```bash
kubectl get pvc -n taskmanager
```

```bash
kubectl get pv
```

```bash
kubectl get storageclass
```

---

# AWS and EKS Commands

Configure AWS credentials:

```bash
aws configure
```

Check AWS identity:

```bash
aws sts get-caller-identity
```

Update EKS kubeconfig:

```bash
aws eks update-kubeconfig \
  --region <region> \
  --name <cluster-name>
```

Check EKS clusters:

```bash
aws eks list-clusters
```

Check node groups:

```bash
aws eks list-nodegroups \
  --cluster-name <cluster-name>
```

---

# Terraform Commands

Initialize:

```bash
terraform init
```

Format:

```bash
terraform fmt -recursive
```

Validate:

```bash
terraform validate
```

Plan:

```bash
terraform plan
```

Apply:

```bash
terraform apply
```

Destroy:

```bash
terraform destroy
```

---

# Docker Commands

Build backend:

```bash
docker build -t taskmanager-backend ./backend
```

Build frontend:

```bash
docker build -t taskmanager-frontend ./frontend
```

List images:

```bash
docker images
```

Run Docker Compose:

```bash
docker compose up --build
```

Stop:

```bash
docker compose down
```

Stop and remove volumes:

```bash
docker compose down --volumes
```

---

# Troubleshooting

## Pod is Pending

Check:

```bash
kubectl describe pod <pod-name> -n taskmanager
```

Common reasons:

* Insufficient node resources
* PVC not bound
* StorageClass problem
* EBS CSI driver issue
* Scheduling constraints

---

# PostgreSQL Pod Not Starting

Check:

```bash
kubectl logs deployment/taskmanager-postgres -n taskmanager
```

Check PVC:

```bash
kubectl get pvc -n taskmanager
```

Check events:

```bash
kubectl get events -n taskmanager --sort-by=.lastTimestamp
```

---

# PVC Stuck in Pending

Check:

```bash
kubectl get pvc -n taskmanager
```

Check:

```bash
kubectl describe pvc <pvc-name> -n taskmanager
```

Check:

```bash
kubectl get storageclass
```

Verify the EBS CSI driver is available:

```bash
aws eks describe-addon \
  --cluster-name <cluster-name> \
  --addon-name aws-ebs-csi-driver
```

---

# Backend Pod CrashLoopBackOff

Check logs:

```bash
kubectl logs <backend-pod> -n taskmanager
```

Check environment variables and secrets:

```bash
kubectl describe pod <backend-pod> -n taskmanager
```

Check PostgreSQL:

```bash
kubectl get pods -n taskmanager
```

The backend depends on PostgreSQL being available.

---

# Frontend Cannot Reach Backend

Check:

```bash
kubectl get svc -n taskmanager
```

Check backend service:

```bash
kubectl describe svc taskmanager-backend -n taskmanager
```

Check frontend Nginx configuration.

The frontend should proxy:

```text
/api/
```

to the backend Kubernetes service.

---

# Jenkins Docker Build Failure

Check that the Jenkins agent has:

```text
Docker
Docker Compose
```

available.

Run:

```bash
docker version
```

and:

```bash
docker compose version
```

---

# Jenkins Cannot Access AWS

Check the Jenkins credential:

```text
aws-credentials
```

Verify that the credential has permissions required for EKS access.

Also verify:

```bash
aws sts get-caller-identity
```

from the Jenkins environment.

---

# Jenkins Cannot Deploy to Kubernetes

Check:

```bash
aws eks update-kubeconfig
```

Then:

```bash
kubectl get nodes
```

Verify that the Jenkins environment can access the EKS API.

---

# Docker Hub Push Failure

Check the Jenkins credential:

```text
dockerhub-credentials
```

Verify the Docker Hub namespace:

```text
DOCKERHUB_NAMESPACE
```

Also verify:

```bash
docker login
```

works from the Jenkins agent.

---

# Updating the Application

To update the application:

```text
1. Modify application code
        |
        v
2. Test locally
        |
        v
3. Commit changes
        |
        v
4. Push to GitHub
        |
        v
5. Jenkins starts
        |
        v
6. Docker images are rebuilt
        |
        v
7. Docker Compose tests run
        |
        v
8. Images are pushed to Docker Hub
        |
        v
9. Jenkins updates EKS deployments
        |
        v
10. Kubernetes performs rolling update
```

The Jenkins build number is used as the image tag.

This makes each deployment traceable to a specific Jenkins build.

---

# Destroying AWS Infrastructure

When the environment is no longer required:

```bash
terraform destroy
```

Terraform will remove the resources managed by the Terraform configuration.

Always review the Terraform plan before destroying infrastructure.

Database and other persistent resources should be treated carefully because destruction can result in data loss.

---

# Current Project Scope

The project intentionally focuses on a manageable set of DevOps technologies.

The current implementation includes:

```text
Application
    |
Docker
    |
Docker Compose
    |
Terraform
    |
AWS
    |
EKS
    |
Kubernetes
    |
Jenkins
    |
Docker Hub
```

The purpose is to demonstrate practical understanding rather than adding a large number of DevOps tools without a real requirement.

---

# Tools Intentionally Not Included

The project does not currently use:

* SonarQube
* Prometheus
* Grafana
* Alertmanager
* ArgoCD
* Helm
* Redis
* Kafka
* Loki
* Service mesh
* Amazon RDS
* Amazon ECR
* HPA
* Multi-region deployment

These tools can be added later if the project requirements expand.

---

# Limitations

The current project is a practical DevOps learning and portfolio project rather than a complete enterprise production platform.

Current limitations include:

* PostgreSQL runs as a single Kubernetes replica
* No database replication
* No automated database backup strategy
* No HPA
* No Prometheus/Grafana monitoring
* No centralized logging
* No automated rollback system
* No multi-region deployment
* No managed RDS database
* Docker Hub is used as the image registry
* Terraform remote S3 state is not currently enabled
* Jenkins deployment is intentionally simple
* Optional Ingress requires a separately installed Nginx Ingress Controller

These limitations are intentional to keep the project understandable and manageable.

---

# Future Improvements

Possible future improvements include:

## Infrastructure

* Enable Terraform remote state using Amazon S3
* Add state locking where appropriate
* Separate environments such as dev/staging/prod
* Improve IAM least-privilege policies
* Add additional networking controls

## Kubernetes

* Add Horizontal Pod Autoscaler
* Add PodDisruptionBudget
* Add NetworkPolicies
* Improve resource tuning
* Add automated rollback

## Database

* Move PostgreSQL to Amazon RDS
* Add automated backups
* Add high availability
* Add database monitoring

## CI/CD

* Add automated security scanning
* Add dependency scanning
* Add automated rollback
* Add deployment approvals
* Add better pipeline notifications

## Observability

* Add Prometheus
* Add Grafana
* Add centralized logging
* Add alerting

## GitOps

A future version could introduce:

* ArgoCD
* GitOps-based Kubernetes deployments
* Separate application and deployment repositories

---

# Current vs Production Architecture

## Current Project

```text
GitHub
   |
   v
Jenkins
   |
   +--> Docker Build
   |
   +--> Docker Compose Test
   |
   +--> Docker Hub
   |
   +--> EKS Deployment
            |
            +--> Frontend
            |
            +--> Backend
            |
            +--> PostgreSQL
                     |
                     +--> EBS
```

## Possible Production Evolution

```text
GitHub
   |
   v
CI Pipeline
   |
   +--> Build
   +--> Test
   +--> Security Scan
   |
   v
Container Registry
   |
   v
GitOps Repository
   |
   v
ArgoCD
   |
   v
Amazon EKS
   |
   +--> Frontend
   +--> Backend
   |
   v
Amazon RDS
   |
   v
Monitoring
   |
   +--> Prometheus
   +--> Grafana
   +--> Logging
```

The second architecture represents possible future improvements and is not the current implementation.

---

# Project Documentation

Additional project documentation is available in the repository.

## DEVOPS-FILES-EXPLAINED.md

Provides explanations of the major DevOps files and configurations.

Topics include:

* Terraform files
* Kubernetes manifests
* Docker files
* Jenkinsfile
* Infrastructure configuration

## INTERVIEW-PROJECT-EXPLANATION.md

Contains project explanations useful for technical interviews.

Topics include:

* Project overview
* Architecture
* DevOps workflow
* AWS infrastructure
* Kubernetes
* Jenkins
* Troubleshooting

## PROJECT-QUESTION-BANK.md

Contains common interview questions related to the project and its technologies.

---

# Contributing

To contribute:

```bash
git checkout -b feature/your-feature
```

Make the required changes.

Test the application locally.

Commit the changes:

```bash
git add .
git commit -m "feat: describe your change"
```

Push the branch:

```bash
git push origin feature/your-feature
```

Create a pull request.

---

# Interview Explanation

## 30-Second Explanation

> This is a cloud-native task management application built with Flask, PostgreSQL, Docker, Kubernetes, Terraform, AWS EKS, and Jenkins. I containerized the frontend and backend using Docker and use Docker Compose for local integration testing. Terraform provisions the AWS networking, EC2, IAM, EKS cluster, and managed node group. The application is deployed on EKS using Kubernetes manifests, with PostgreSQL using persistent EBS storage through the EBS CSI driver. Jenkins automates the process of building Docker images, testing them with Docker Compose, pushing them to Docker Hub, and deploying the new image versions to EKS.

---

# 2-Minute Explanation

> The project is a task management application with a Flask backend, PostgreSQL database, and Nginx-based frontend.
>
> I started by containerizing the application. The backend runs using Gunicorn and the frontend is served through Nginx. Docker Compose is used locally to run PostgreSQL, backend, and frontend together.
>
> For AWS infrastructure, I used Terraform. Terraform creates a VPC with public and private subnets across multiple Availability Zones, an Internet Gateway, NAT Gateway, route tables, security groups, an EC2 operational host, IAM roles, an Amazon EKS cluster, and a managed node group.
>
> The EKS worker nodes run in private subnets. The EKS API endpoint has public and private access enabled, with public access restricted using configurable CIDRs.
>
> On Kubernetes, I created a separate namespace for the application. The frontend, backend, and PostgreSQL run as separate deployments. PostgreSQL uses a PersistentVolumeClaim backed by AWS EBS through the EBS CSI driver, so database data is not stored only inside the container.
>
> For CI/CD, Jenkins checks out the code, builds the frontend and backend Docker images, runs the application using Docker Compose for a basic integration test, pushes the images to Docker Hub using the Jenkins build number as the image tag, and then deploys the new images to EKS.
>
> Jenkins also creates the required Kubernetes Secrets and ensures the EBS CSI add-on is available before deploying the PostgreSQL storage.
>
> The project intentionally keeps the application architecture simple so the main focus is on practical DevOps concepts such as Terraform, AWS networking, Docker, Kubernetes, EKS, persistent storage, Jenkins, and deployment troubleshooting.

---

# Key DevOps Concepts Demonstrated

This project demonstrates practical understanding of:

## Docker

* Writing Dockerfiles
* Building images
* Running containers
* Docker Compose
* Container networking
* Multi-container applications

## Terraform

* Infrastructure as Code
* Terraform variables
* AWS provider
* VPC creation
* Subnets
* Route tables
* NAT Gateway
* Security groups
* IAM
* EKS
* Managed node groups

## AWS

* VPC
* EC2
* IAM
* EKS
* EBS
* Availability Zones
* Public/private networking
* NAT Gateway
* Security Groups

## Kubernetes

* Namespace
* Deployment
* Service
* ClusterIP
* LoadBalancer
* PersistentVolumeClaim
* StorageClass
* Secrets
* Probes
* Resource requests/limits
* Rolling updates

## Jenkins

* Pipeline stages
* Credentials
* Docker builds
* Automated testing
* Docker Hub publishing
* AWS authentication
* kubectl deployment
* Rollout verification

---

# Important Ports

| Component        | Port | Purpose               |
| ---------------- | ---: | --------------------- |
| Frontend / Nginx |   80 | Web application       |
| Backend          | 8888 | Flask API             |
| PostgreSQL       | 5432 | Database              |
| Jenkins          | 8080 | Jenkins web interface |
| Kubernetes API   |  443 | Kubernetes API        |

---

# Important Kubernetes Resources

| Resource              | Name / Purpose         |
| --------------------- | ---------------------- |
| Namespace             | `taskmanager`          |
| Backend Deployment    | Flask backend          |
| Frontend Deployment   | Nginx frontend         |
| PostgreSQL Deployment | PostgreSQL database    |
| Backend Service       | ClusterIP              |
| Frontend Service      | LoadBalancer           |
| PostgreSQL Service    | ClusterIP              |
| PostgreSQL PVC        | 5Gi persistent storage |
| StorageClass          | `taskmanager-gp3`      |
| Ingress               | Optional Nginx routing |

---

# Important AWS Resources

The Terraform configuration creates resources including:

* VPC
* Public subnets
* Private subnets
* Internet Gateway
* NAT Gateway
* Route tables
* Security groups
* EC2 instance
* IAM roles
* EKS cluster
* EKS managed node group

The EKS node group uses private subnets.

---

# Important Jenkins Flow

```text
GitHub
   |
   v
Checkout
   |
   v
Build Docker Images
   |
   v
Docker Compose Test
   |
   v
Push to Docker Hub
   |
   v
Configure EKS
   |
   v
Deploy Kubernetes Resources
   |
   v
Update Image Tags
   |
   v
Wait for Rollout
   |
   v
Verify Pods and Services
```

---

# Important Troubleshooting Flow

When an application is not working:

```text
1. Check nodes
       |
       v
2. Check pods
       |
       v
3. Check pod status
       |
       v
4. Check pod logs
       |
       v
5. Describe the pod
       |
       v
6. Check services
       |
       v
7. Check PVC
       |
       v
8. Check storage class
       |
       v
9. Check EBS CSI driver
       |
       v
10. Check application configuration
```

Useful commands:

```bash
kubectl get nodes
kubectl get pods -n taskmanager
kubectl get svc -n taskmanager
kubectl get pvc -n taskmanager
kubectl get events -n taskmanager
kubectl logs <pod> -n taskmanager
kubectl describe pod <pod> -n taskmanager
```

---

# Summary

Cloud-Native Task Manager demonstrates an end-to-end DevOps workflow for deploying a containerized application on AWS.

The project combines:

```text
Flask
   +
PostgreSQL
   +
Nginx
   +
Docker
   +
Docker Compose
   +
Terraform
   +
AWS
   +
Kubernetes
   +
Amazon EKS
   +
EBS CSI
   +
Jenkins
   +
Docker Hub
```

The complete workflow is:

```text
Developer
    |
    v
GitHub
    |
    v
Jenkins
    |
    +------------------+
    |                  |
    v                  v
Docker Build      Docker Compose Test
    |
    v
Docker Hub
    |
    v
Amazon EKS
    |
    +-------------------+
    |                   |
    v                   v
Frontend             Backend
    |                   |
    +---------+---------+
              |
              v
         PostgreSQL
              |
              v
          AWS EBS
```

The project focuses on practical DevOps fundamentals rather than adding unnecessary technologies.

It provides hands-on experience with:

* Containerization
* Infrastructure as Code
* AWS networking
* EKS
* Kubernetes
* Persistent storage
* CI/CD
* Docker image management
* Secrets
* Health checks
* Rolling deployments
* Troubleshooting

---
