pipeline {
    agent any

    //image tag used with git commit id
    environment {
        IMAGE_TAG = "${GIT_COMMIT.take(7)}"
    }

    stages {

        stage('Test Service A') {
            steps {
                sh '''
                docker run --rm \
                  -v "$PWD/microservices/service-a:/app" \
                  -w /app \
                  python:3.12-slim \
                  sh -c "pip install -r requirements.txt && python -m pytest"
                '''
            }
        }

        stage('Test Service B') {
            steps {
                sh '''
                docker run --rm \
                  -v "$PWD/microservices/service-b:/app" \
                  -w /app \
                  python:3.12-slim \
                  sh -c "pip install -r requirements.txt && python -m pytest"
                '''
            }
        }

        stage('Build Service A') {
            steps {
                sh '''
                docker build \
                  -t nganudeep99/service-a:${IMAGE_TAG} \
                  ./microservices/service-a
                '''
            }
        }

        stage('Build Service B') {
            steps {
                sh '''
                docker build \
                  -t nganudeep99/service-b:${IMAGE_TAG} \
                  ./microservices/service-b
                '''
            }
        }

        stage('Trivy Scan Service A') {
            steps {
                sh '''
                trivy image \
                  --severity HIGH,CRITICAL \
                  --ignore-unfixed \
                  --exit-code 1 \
                  nganudeep99/service-a:${IMAGE_TAG}
                '''
            }
        }

        stage('Trivy Scan Service B') {
            steps {
                sh '''
                trivy image \
                  --severity HIGH,CRITICAL \
                  --ignore-unfixed \
                  --exit-code 1 \
                  nganudeep99/service-b:${IMAGE_TAG}
                '''
            }
        }

        stage('Docker Hub Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKERHUB_USERNAME',
                    passwordVariable: 'DOCKERHUB_TOKEN'
                )]) {
                    sh '''
                    echo "$DOCKERHUB_TOKEN" | docker login \
                      -u "$DOCKERHUB_USERNAME" \
                      --password-stdin
                    '''
                }
            }
        }

        stage('Push Service A') {
            steps {
                sh '''
                docker push nganudeep99/service-a:${IMAGE_TAG}
                '''
            }
        }

        stage('Push Service B') {
            steps {
                sh ''' 
                docker push nganudeep99/service-b:${IMAGE_TAG}
                '''
            }
        }

// Update GitOps repo with the new image SHA
        stage('Update GitOps') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'github-gitops-push',
                    usernameVariable: 'GITHUB_USERNAME',
                    passwordVariable: 'GITHUB_TOKEN'
                )]) {
                    sh '''
                    rm -rf gitops
                    git clone https://${GITHUB_USERNAME}:${GITHUB_TOKEN}@github.com/nganudeeep/Devsecops-gitops.git gitops

                    sed -i.bak "s/tag: \\"1.0\\"/tag: \\"${IMAGE_TAG}\\"/" gitops/environments/dev/values-service-a.yaml
                    sed -i.bak "s/tag: \\"1.0\\"/tag: \\"${IMAGE_TAG}\\"/" gitops/environments/dev/values-service-b.yaml

                    rm -f gitops/environments/dev/*.bak

                    cd gitops
                    git config user.name "Jenkins"
                    git config user.email "jenkins@localhost"

                    git add environments/dev/values-service-a.yaml environments/dev/values-service-b.yaml
                    git commit -m "Update dev images to ${IMAGE_TAG}"
                    git push origin main
                    '''
                }
            }
        }
    }
}