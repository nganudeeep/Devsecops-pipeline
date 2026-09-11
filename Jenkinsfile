pipeline {
    agent any

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
                  -t nganudeep99/service-a:1.0 \
                  ./microservices/service-a
                '''
            }
        }

        stage('Build Service B') {
            steps {
                sh '''
                docker build \
                  -t nganudeep99/service-b:1.0 \
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
                  nganudeep99/service-a:1.0
                '''
            }
        }

        stage('Trivy Scan Service B') {
            steps {
                sh '''
                trivy image \
                  --severity HIGH,CRITICAL \
                  --ignore-unfixed \
                  nganudeep99/service-b:1.0
                '''
            }
        }
    }
}