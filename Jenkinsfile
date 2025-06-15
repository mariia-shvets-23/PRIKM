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
                echo "Lab-1: ${env.IMAGE_NAME}"
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
                    # створюємо і активуємо venv
                    python3 -m venv venv
                    . venv/bin/activate

                    # оновлюємо pip та встановлюємо pytest
                    pip install --upgrade pip
                    pip install -r tests/requirements.txt

                    # запускаємо тести
                    pytest -q tests
                '''
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // зупиняємо старий контейнер на 80
                    sh '''
                        container_id=$(docker ps -q --filter "publish=80")
                        if [ -n "$container_id" ]; then
                            docker stop $container_id
                            docker rm   $container_id
                        fi
                    '''
                    // запускаємо новий контейнер на відповідному порту
                    if (env.TARGET_ENV == 'production') {
                        sh "docker run -d -p 80:80 ${env.IMAGE_NAME}:latest"
                    } else {
                        sh "docker run -d -p 8081:80 ${env.IMAGE_NAME}:latest"
                    }
                }
            }
        }
    }
}
