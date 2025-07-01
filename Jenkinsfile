pipeline {
    agent any

    environment {
        IMAGE_NAME = 'jenkins1-app'
        CONTAINER_NAME = 'jenkins1-container'
        PORT = '8501'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git url: 'https://github.com/mnasar1/Jenkins1.git', branch: 'master'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                    docker rm -f $CONTAINER_NAME || true
                    docker run -d -p $PORT:8501 --name $CONTAINER_NAME $IMAGE_NAME
                '''
            }
        }
    }
}

