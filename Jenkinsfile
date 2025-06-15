pipeline {
    agent any
    environment {
        IMAGE_NAME = 'nginx/custom'
    }
    stages {
        stage('Set Target Environment') {
            steps {
                script {
                    if (env.GIT_BRANCH == 'origin/main' || env.GIT_BRANCH == 'origin/master') {
                        env.TARGET_ENV = 'production'
                    } else {
                        env.TARGET_ENV = 'development'
                    }
                    echo "Target environment: ${env.TARGET_ENV}"
                }
            }
        }

        stage('Start') {
            steps {
                echo "Lab_1: ${env.IMAGE_NAME}"
            }
        }

        stage('Build') {
            steps {
                sh "docker build -t ${env.IMAGE_NAME}:latest ."
            }
        }
        stage('Test') {
            steps {
                sh '''
                    # Встановити Python 3 і pip (якщо ще не встановлено)
                    apt-get update && apt-get install -y python3 python3-pip
        
                    # Встановити залежності для тестів
                    pip3 install --upgrade pip
                    pip3 install -r tests/requirements.txt
        
                    # Запуск тестів
                    python3 -m pytest -q tests
                '''
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Зупинити старий контейнер на 80 порту
                    sh '''
                        container_id=$(docker ps -q --filter "publish=80")
                        if [ -n "$container_id" ]; then
                            echo "Stopping container using port 80: $container_id"
                            docker stop $container_id
                            docker rm $container_id
                        fi
                    '''
                    // Запустити новий контейнер
                    if (env.TARGET_ENV == 'production') {
                        sh "docker run -d -p 80:80 ${env.IMAGE_NAME}:latest"
                    } else {
                        sh "docker run -d -p 8080:80 ${env.IMAGE_NAME}:latest"
                    }
                }
            }
        }
    }
}
