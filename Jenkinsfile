pipeline {
    agent any

    environment {
        REGISTRY     = 'mariia/nginx-custom'
        TAG          = "${env.BUILD_NUMBER}"
        TARGET_ENV   = (env.GIT_BRANCH ==~ /origin\\/main|origin\\/master/ ? 'production' : 'development')
    }

    stages {
        stage('Checkout') { steps { checkout scm } }

        stage('Install & Test') {
            steps {
                sh 'pip install -r requirements.txt --quiet'
                sh 'pytest -q'
            }
        }

        stage('Build image') {
            steps {
                sh """
                   docker build -t ${REGISTRY}:${TAG} .
                   docker tag ${REGISTRY}:${TAG} ${REGISTRY}:${TARGET_ENV}
                """
            }
        }

        stage('Deploy') {
            steps {
                script {
                    def port = TARGET_ENV == 'production' ? '80' : '8081'
                    def name = TARGET_ENV == 'production' ? 'prod_app' : 'dev_app'
                    sh """
                        cid=\$(docker ps -q --filter "name=${name}") || true
                        [ -n "\$cid" ] && docker rm -f \$cid
                        docker run -d --name ${name} -p ${port}:80 ${REGISTRY}:${TARGET_ENV}
                    """
                }
            }
        }
    }

    post {
        success { echo "Deploy ${TARGET_ENV} complete" }
        failure { echo "Pipeline failed" }
    }
}
