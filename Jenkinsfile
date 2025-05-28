properties([
    office365ConnectorWebhooks([
        [
            name: 'Teams-O365',
            url: 'https://lpnu.webhook.office.com/webhookb2/cdb8219e-a982-4020-96bc-0cb927b5c250@7631cd62-5187-4e15-8b8e-ef653e366e7a/JenkinsCI/d362810701ac415cabf8dbc577233ed7/294e4ebb-5ec1-414e-8bf6-c622514c87e0/V20PBAjwS-hjJPEVvl0shJOKSkDEdKM1EEADmXJeEjMVg1',
            startNotification: false,
            notifySuccess: true,
            notifyAborted: false,
            notifyNotBuilt: false,
            notifyUnstable: true,
            notifyFailure: true,
            notifyBackToNormal: true,
            notifyRepeatedFailure: false,
            timeout: 30000
        ]
    ])
])

pipeline {
    agent any

    options {
        ansiColor('xterm') // Включає кольоровий вивід
    }

    parameters {
        choice(name: 'ENV', choices: ['dev', 'test', 'prod'], description: 'Choose environment')
        string(name: 'MESSAGE', defaultValue: 'Hello from Jenkins!', description: 'Message to send to Teams')
    }

    triggers {
        cron('H/5 * * * *')
    }

    stages {
        stage('Print to Console') {
            steps {
                echo "\u001B[32m✔ Pipeline started\u001B[0m"
                echo "\u001B[36mSelected environment: ${params.ENV}\u001B[0m"
                echo "\u001B[35mMessage: ${params.MESSAGE}\u001B[0m"
            }
        }

        stage('Save to File') {
            steps {
                script {
                    def content = "Environment: ${params.ENV} | Message: ${params.MESSAGE}"
                    writeFile file: 'log.txt', text: content
                }
            }
        }

        stage('Send Message to Teams') {
            steps {
                office365ConnectorSend webhookUrl: 'https://lpnu.webhook.office.com/webhookb2/cdb8219e-a982-4020-96bc-0cb927b5c250@7631cd62-5187-4e15-8b8e-ef653e366e7a/JenkinsCI/d362810701ac415cabf8dbc577233ed7/294e4ebb-5ec1-414e-8bf6-c622514c87e0/V20PBAjwS-hjJPEVvl0shJOKSkDEdKM1EEADmXJeEjMVg1',
                                       message: "🚀 Jenkins notification\n• Environment: ${params.ENV}\n• Message: ${params.MESSAGE}",
                                       status: 'Success'
            }
        }
    }
}
