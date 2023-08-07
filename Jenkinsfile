pipeline {
    agent any

    environment {
        DOCKER_HUB_REPO = 'ahmetozleraktas/simple-flask-app'
        IMAGE_TAG = 'latest'
        DOCKERHUB_CREDENTIALS = credentials('dockerhub_login')
    }

    stages {
        stage('SCM Checkout') {
            steps {
                // Checkout source code from your repository
                sh 'git clone https://github.com/ahmetozleraktas/devops-project-gke.git'
            }
            
            // Build the Docker image
                
        }
        stage('Build Docker image') {
            steps {
                sh "docker build -t ${DOCKER_HUB_REPO}:${IMAGE_TAG} ."
            }
        }

        stage('Login to DockerHub') {
            steps {
                sh 'echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin'
            }
        }

        stage('Push to DockerHub') {
            steps {
                sh "docker push ${DOCKER_HUB_REPO}:${IMAGE_TAG}"
            }
        }
    }
}

post {
    always {
        sh 'docker logout'
    }
}
