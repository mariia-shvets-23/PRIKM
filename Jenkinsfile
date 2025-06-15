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
                    // 1) Прибираємо старий PROD (порт 80), якщо є
                    sh '''
                        cid80=$(docker ps -q --filter "publish=80")
                        [ -n "$cid80" ] && docker rm -f $cid80
                    '''
        
                    if (env.TARGET_ENV == 'production') {
                        // 2a) Запускаємо prod на 80
                        sh "docker run -d -p 80:80 ${env.IMAGE_NAME}:latest"
                    } else {
                        // 2b) Спочатку зупиняємо старий DEV (порт 8081), якщо є
                        sh '''
                            cid8081=$(docker ps -q --filter "publish=8081")
                            [ -n "$cid8081" ] && docker rm -f $cid8081
                        '''
                        // 3) Запускаємо DEV на 8081
                        sh "docker run -d -p 8081:80 ${env.IMAGE_NAME}:latest"
                    }
                }
            }
        }
    }
}
