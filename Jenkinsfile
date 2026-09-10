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
    }
}