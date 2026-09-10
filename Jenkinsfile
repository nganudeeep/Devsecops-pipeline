pipeline {
    agent any

    stages {

        stage('Checkout'){
            steps{
                checkout scm
            }
        }

        stage('Test Service A') {
            steps {
                sh 'cd microservices/service-a && python -m pytest'
            }
        }

        stage('Test Service B') {
            steps {
                sh 'cd microservices/service-b && python -m pytest'
            }
        }
    }
}