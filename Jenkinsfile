                                                    pipeline {
                                                        agent any

                                                        parameters {
                                                            string(name: 'DOCKERHUB_NAMESPACE', defaultValue: '', description: 'Docker Hub namespace used for published images')
                                                            string(name: 'AWS_REGION', defaultValue: 'us-east-1', description: 'AWS region containing the EKS cluster')
                                                            string(name: 'EKS_CLUSTER_NAME', defaultValue: 'taskmanager-eks', description: 'EKS cluster name')
                                                        }

                                                        environment {
                                                            POSTGRES_USER = 'taskmanager'
                                                            POSTGRES_DB = 'taskmanager_db'
                                                        }

                                                        stages {
                                                            stage('Checkout') {
                                                                steps {
                                                                    checkout scm
                                                                }
                                                            }

                                                            stage('Build Images') {
                                                                steps {
                                                                    sh '''
                                                                        set -eu
                                                                        : "${DOCKERHUB_NAMESPACE:?Set the DOCKERHUB_NAMESPACE build parameter}"
                                                                        docker build -t "$DOCKERHUB_NAMESPACE/taskmanager-backend:$BUILD_NUMBER" backend
                                                                        docker build -t "$DOCKERHUB_NAMESPACE/taskmanager-frontend:$BUILD_NUMBER" frontend
                                                                    '''
                                                                }
                                                            }

                                                            stage('Test with Docker Compose') {
                                                                steps {
                                                                    withCredentials([
                                                                        string(credentialsId: 'taskmanager-db-password', variable: 'POSTGRES_PASSWORD'),
                                                                        string(credentialsId: 'taskmanager-app-secret-key', variable: 'SECRET_KEY')
                                                                    ]) {
                                                                        sh '''
                                                                            set +x
                                                                            set -eu
                                                                            trap 'docker compose down --volumes' EXIT
                                                                            docker compose up -d --build

                                                                            attempt=0
                                                                            until curl -fsS http://localhost:8888/api/health; do
                                                                                attempt=$((attempt + 1))
                                                                                [ "$attempt" -lt 30 ] || exit 1
                                                                                sleep 2
                                                                            done
                                                                            curl -fsS http://localhost/
                                                                        '''
                                                                    }
                                                                }
                                                            }

                                                            stage('Push Images') {
                                                                steps {
                                                                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                                                                        sh '''
                                                                                set +x
                                                                            set -eu
                                                                                printf '%s' "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                                                                            docker push "$DOCKERHUB_NAMESPACE/taskmanager-backend:$BUILD_NUMBER"
                                                                            docker push "$DOCKERHUB_NAMESPACE/taskmanager-frontend:$BUILD_NUMBER"
                                                                        '''
                                                                    }
                                                                }
                                                            }

                                                            stage('Deploy to EKS') {
                                                                steps {
                                                                    withCredentials([
                                                                        [$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-credentials'],
                                                                        string(credentialsId: 'taskmanager-db-password', variable: 'POSTGRES_PASSWORD'),
                                                                        string(credentialsId: 'taskmanager-app-secret-key', variable: 'SECRET_KEY')
                                                                    ]) {
                                                                        sh '''
                                                                            set +x
                                                                            set -eu
                                                                            aws eks update-kubeconfig --name "$EKS_CLUSTER_NAME" --region "$AWS_REGION"
                                                                            kubectl apply -f k8s/namespace.yaml
                                                                            if ! aws eks describe-addon --cluster-name "$EKS_CLUSTER_NAME" --addon-name aws-ebs-csi-driver --region "$AWS_REGION" >/dev/null 2>&1; then
                                                                                aws eks create-addon --cluster-name "$EKS_CLUSTER_NAME" --addon-name aws-ebs-csi-driver --region "$AWS_REGION"
                                                                            fi
                                                                            aws eks wait addon-active --cluster-name "$EKS_CLUSTER_NAME" --addon-name aws-ebs-csi-driver --region "$AWS_REGION"
                                                                            kubectl apply -f k8s/storage-class.yaml

                                                                            umask 077
                                                                            secret_dir=$(mktemp -d)
                                                                            trap 'rm -rf "$secret_dir"' EXIT
                                                                            printf 'password=%s\n' "$POSTGRES_PASSWORD" > "$secret_dir/postgres.env"
                                                                            printf 'secret-key=%s\n' "$SECRET_KEY" > "$secret_dir/backend.env"
                                                                            kubectl create secret generic postgres-secret -n taskmanager --from-env-file="$secret_dir/postgres.env" --dry-run=client -o yaml | kubectl apply -f -
                                                                            kubectl create secret generic backend-secret -n taskmanager --from-env-file="$secret_dir/backend.env" --dry-run=client -o yaml | kubectl apply -f -

                                                                            kubectl apply -f k8s/postgres-pvc.yaml
                                                                            kubectl apply -f k8s/postgres-deployment.yaml
                                                                            kubectl rollout status deployment/postgres -n taskmanager --timeout=300s

                                                                            kubectl apply -f k8s/backend-deployment.yaml
                                                                            kubectl apply -f k8s/frontend-deployment.yaml
                                                                            kubectl apply -f k8s/ingress.yaml
                                                                            kubectl set image deployment/backend backend="$DOCKERHUB_NAMESPACE/taskmanager-backend:$BUILD_NUMBER" -n taskmanager
                                                                            kubectl set image deployment/frontend frontend="$DOCKERHUB_NAMESPACE/taskmanager-frontend:$BUILD_NUMBER" -n taskmanager
                                                                            kubectl rollout status deployment/backend -n taskmanager --timeout=300s
                                                                            kubectl rollout status deployment/frontend -n taskmanager --timeout=300s
                                                                            kubectl get pods,services -n taskmanager
                                                                        '''
                                                                    }
                                                                }
                                                            }
                                                        }

                                                        post {
                                                            always {
                                                                sh 'docker logout || true'
                                                                cleanWs()
                                                            }
                                                            success {
                                                                echo 'CI/CD pipeline completed successfully.'
                                                            }
                                                            failure {
                                                                echo 'CI/CD pipeline failed. Check the build logs.'
                                                            }
                                                        }
                                                    }
