# Terraform Infrastructure

This configuration provisions the project's AWS VPC, public and private subnets, NAT gateway, EC2 host, and EKS cluster with a managed node group. It uses the AWS credentials configured in your environment; no AWS account ID or access key is stored here.

## Configure and Apply

1. Install Terraform 1.5 or newer and configure AWS CLI credentials with the required permissions.
2. Copy `terraform.tfvars.example` to `terraform.tfvars`. Set a valid AMI and EKS version for the selected region, and update subnet CIDRs and availability zones as needed.
3. Generate an SSH key pair using the configured `ec2_key_pair_name`; place the public key at `keys/<key-name>.pub`. Never put the private key in this repository.
4. Add your public IP in CIDR notation (for example, `/32`) to `allowed_ssh_cidrs` if you need EC2 SSH and Jenkins access. The default opens neither port to the internet.
5. Run:

```sh
terraform init
terraform fmt -check
terraform validate
terraform plan
terraform apply
```

Review the plan carefully. EKS, NAT gateways, and EC2 incur AWS charges. Use `terraform destroy` when finished with a disposable environment.

Terraform state, local variable files, and private keys are ignored by Git. For shared deployments, configure an encrypted remote state backend and state locking before applying.
