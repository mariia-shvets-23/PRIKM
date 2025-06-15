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
                    if (env.TARGET_ENV == 'production') {
                        // Очистити порт 80
                        sh '''
                            cid=$(docker ps -q --filter "publish=80")
                            if [ -n "$cid" ]; then
                                docker rm -f $cid
                            fi
                        '''
                        // Запустити продакшн
                        sh "docker run -d -p 80:80 ${env.IMAGE_NAME}:latest"
                    } else {
                        // Очистити порт 8081
                        sh '''
                            cid=$(docker ps -q --filter "publish=8081")
                            if [ -n "$cid" ]; then
                                docker rm -f $cid
                            fi
                        '''
                        // Запустити дев
                        sh "docker run -d -p 8081:80 ${env.IMAGE_NAME}:latest"
                    }
                }
            }
        }
    }
}
