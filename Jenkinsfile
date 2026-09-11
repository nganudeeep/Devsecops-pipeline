pipeline {
    agent any

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
    }
}