pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
        IMAGE_NAME = 'vishruthere/scientific-calculator'
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Clone Repository') {
            steps {
                echo 'Cloning source code from GitHub...'
                git branch: 'main',
                    url: 'https://github.com/KumarTheVishrut/scientific-calculator.git'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running PyUnit tests...'
                sh 'python3 -m unittest test_calculator -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image: ${IMAGE_NAME}:${IMAGE_TAG}"
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                sh "docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest"
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo 'Pushing image to Docker Hub...'
                sh "echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin"
                sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                sh "docker push ${IMAGE_NAME}:latest"
            }
        }

        stage('Deploy with Ansible') {
            steps {
                echo 'Deploying via Ansible playbook...'
                sh 'ansible-playbook -i inventory.ini deploy.yml'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up Docker login session...'
            sh 'docker logout'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs above.'
        }
    }
}
