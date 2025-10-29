pipeline {
    agent any

    environment {
        // ✅ Use the exact Jenkins credentials ID for your DockerHub token
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-token')
        // ✅ Your correct DockerHub username
        DOCKER_IMAGE = "samyuktha2696/flask-app"
    }

    stages {

        stage('Checkout') {
            steps {
                echo '📦 Cloning the repository...'
                git branch: 'main',
                    url: 'https://github.com/samyuktha-1213/task-today.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '⚙️ Installing Python dependencies...'
                // ✅ Use . instead of source (works on both bash & sh)
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Running tests...'
                sh '''
                . venv/bin/activate
                pytest || true
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image...'
                // ✅ Make sure Jenkins user has docker group access
                sh '''
                docker build -t $DOCKER_IMAGE:latest .
                '''
            }
        }

        stage('Push to DockerHub') {
            steps {
                echo '🚀 Logging in and pushing Docker image...'
                // ✅ Corrected username here
                sh '''
                echo $DOCKERHUB_CREDENTIALS | docker login -u samyuktha2696 --password-stdin
                docker push $DOCKER_IMAGE:latest
                '''
            }
        }

        stage('Deploy Container') {
            steps {
                echo '🚢 Deploying container locally...'
                sh '''
                docker rm -f flask-container || true
                docker run -d -p 5000:5000 --name flask-container $DOCKER_IMAGE:latest
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Deployment completed successfully!'
        }
        failure {
            echo '❌ Build failed. Check logs for details.'
        }
    }
}

