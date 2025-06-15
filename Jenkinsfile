pipeline {
    agent any
    environment {
        IMAGE_NAME = 'nginx/custom'
    }
    stages {
        stage('Set Target Environment') {
            steps {
                script {
                    env.TARGET_ENV = (env.GIT_BRANCH == 'origin/main' || env.GIT_BRANCH == 'origin/master') ? 'production' : 'development'
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
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r tests/requirements.txt
                    pytest -q tests
                '''
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // прибрати старий prod-контейнер (якщо був на 80)
                    sh '''
                        cid=$(docker ps -q --filter "publish=80")
                        [ -n "$cid" ] && docker rm -f $cid
                    '''
                    if (env.TARGET_ENV == 'production') {
                        sh "docker run -d -p 80:80 ${env.IMAGE_NAME}:latest"
                    } else {
                        sh "docker run -d -p 8081:80 ${env.IMAGE_NAME}:latest"
                    }
                }
            }
        }