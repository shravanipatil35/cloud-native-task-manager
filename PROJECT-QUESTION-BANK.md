# Project Question Bank: Cloud-Native Task Manager

## Multiple Choice

1. Which service stores application data?<br>
   A. Nginx  B. PostgreSQL  C. Jenkins  D. Terraform<br>
   **Answer: B**

2. What does Docker Compose provide for local development?<br>
   A. A multi-container local stack  B. An AWS account  C. Kubernetes node scaling  D. Source control<br>
   **Answer: A**

3. Which component serves the static frontend?<br>
   A. Flask  B. PostgreSQL  C. Nginx  D. Terraform<br>
   **Answer: C**

4. Where should the local Flask session key be configured?<br>
   A. In a committed Kubernetes manifest  B. In the ignored `.env` file  C. In the Dockerfile  D. In a source comment<br>
   **Answer: B**

5. What does a Kubernetes Service provide?<br>
   A. A stable network endpoint for selected pods  B. An AWS IAM user  C. A container image  D. A Terraform state file<br>
   **Answer: A**

6. What does the PostgreSQL persistent volume claim provide?<br>
   A. Persistent storage for database files  B. A frontend route  C. Jenkins credentials  D. A Docker registry<br>
   **Answer: A**

7. What is Terraform used for in this repository?<br>
   A. Provisioning AWS infrastructure  B. Serving HTML  C. Running SQL queries  D. Building Python packages<br>
   **Answer: A**

8. Why does the pipeline use build-number image tags?<br>
   A. To identify and deploy a specific build  B. To encrypt images  C. To create a Kubernetes namespace  D. To assign an AWS region<br>
   **Answer: A**

9. Where do pipeline credentials belong?<br>
   A. Jenkins Credentials  B. A tracked `.tfvars` file  C. The Dockerfile  D. Kubernetes labels<br>
   **Answer: A**

10. What does a rollout status check verify?<br>
    A. That a Deployment reaches its desired state  B. That Terraform is installed  C. That a GitHub account exists  D. That a local database was deleted<br>
    **Answer: A**

## Scenario Questions

1. **The backend cannot connect to PostgreSQL in Compose. What do you check?**<br>
   Confirm the Compose service name is used as the database host, the password and database name match in both services, PostgreSQL is healthy, and the backend environment values are set.

2. **The app fails immediately in production because a setting is missing. Why is that useful?**<br>
   Production requires a session key and database credentials. Failing at startup avoids silently using a development key or local SQLite database.

3. **A PostgreSQL pod remains pending because its claim is unbound. What do you inspect?**<br>
   Check the claim events, storage class, EBS CSI add-on status, and the worker-node IAM permissions required by the driver.

4. **A Kubernetes image pull fails. What do you verify?**<br>
   Confirm the pushed image name and build tag match the Deployment, the repository exists, and the repository is public or cluster pull credentials are configured.

5. **The Jenkins deployment stage cannot access EKS. What do you check?**<br>
   Verify the AWS Jenkins credential, selected region and cluster name, IAM permissions, and the identity's Kubernetes access authorization.

6. **The Terraform plan opens SSH to everyone. What should you do?**<br>
   Set `allowed_ssh_cidrs` to the operator's public IP with a `/32` suffix, then review the plan again before applying.

7. **The application rollout succeeds but the Ingress has no address. What may be missing?**<br>
   The cluster may not have an ingress controller configured for the `nginx` class. The frontend LoadBalancer Service is independent of that Ingress.

8. **A local change appears to be lost after restarting Compose. What do you check?**<br>
   Confirm PostgreSQL is using the named volume and that the volume was not explicitly removed with `docker compose down -v`.

## Discussion Prompts

- How does a Kubernetes Deployment recover when a container exits?
- Why should stateful PostgreSQL storage be separated from the container filesystem?
- Which resources in the Terraform plan have ongoing AWS cost?
- How would you configure a remote, encrypted Terraform state backend for a team?
- How would you rotate the Jenkins database password and session key?
- What is the difference between a ClusterIP Service and a LoadBalancer Service?
- Why should Terraform plans be reviewed before applying them?
- How can readiness and liveness probes help a rolling deployment?
- What information should be checked when an HTTP health probe fails?
- How can build tags help roll back an application deployment?
