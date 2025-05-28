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

    triggers {
        cron('H/5 * * * *') // кожні 5 хвилин
    }

    stages {
        stage('Test Notification') {
            steps {
                echo '🔧 Тестуємо інтеграцію з Teams...'
            }
        }
    }
}
