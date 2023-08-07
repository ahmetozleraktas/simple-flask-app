pipeline {
    agent any

    environment {
        DOCKER_HUB_REPO = 'ahmetozleraktas/simple-flask-app'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Build') {
            steps {
                // Checkout source code from your repository
                git 'https://github.com/ahmetozleraktas/simple-flask-app.git'

                // Build the Docker image
                script {
                    def dockerImage = docker.build("${DOCKER_HUB_REPO}:${IMAGE_TAG}")
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                // Log in to DockerHub using your credentials (configure DockerHub credentials in Jenkins)
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub_login') {
                        // Push the Docker image to DockerHub
                        dockerImage.push("${IMAGE_TAG}")
                    }
                }
            }
        }
    }
}
