pipeline {
    agent any
    stages {
        stage('Start') {
            steps {
                echo 'Lab_1: nginx/custom'
                echo 'Webhook trigger test'
            }
        }
        stage('Build nginx/custom') {
            steps {
                sh 'docker build -t nginx/custom:latest .'
            }
        }
        stage('Test nginx/custom') {
            steps {
                echo 'Pass'
            }
        }
        stage('Deploy nginx/custom') {
            steps {
                script {
                    // Знайти контейнер, що слухає порт 80, і зупинити+видалити його
                    sh '''
                        container_id=$(docker ps -q --filter "publish=80")
                        if [ -n "$container_id" ]; then
                            echo "Stopping container using port 80: $container_id"
                            docker stop $container_id
                            docker rm $container_id
                        fi
                    '''
                    // Запустити новий контейнер
                    sh 'docker run -d -p 80:80 nginx/custom:latest'
                }
            }
        }
    }
}
