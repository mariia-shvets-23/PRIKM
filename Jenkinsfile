pipeline {
    agent any

    stages {
        stage('Start') {
            steps {
                echo 'Lab_2: started by GitHub'
            }
        }
        stage('Build image') {
            steps {
                sh 'docker build -t prikm:latest .'
                sh 'docker tag prikm mariiashvets/prikm:latest'
                sh 'docker tag prikm mariiashvets/prikm:${BUILD_NUMBER}'
            }
        }
        stage('Push to DockerHub') {
            steps {
                withDockerRegistry([ credentialsId: 'dockerhub-creds', url: '' ]) {
                    sh 'docker push mariiashvets/prikm:latest'
                    sh 'docker push mariiashvets/prikm:${BUILD_NUMBER}'
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -d -p 80:80 mariiashvets/prikm'
            }
        }
    }
}
