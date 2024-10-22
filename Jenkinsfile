pipeline {
    agent any
    environment {
        SERVER_CRED = credentials('cred')  // Bind credentials to this environment variable
    }
    stages {
        parallel {
            stage("username") {
                steps {
                    sh "echo 'Username is ${SERVER_CRED_USR}'"
                }
            }

            stage("password") {
                steps {
                    sh "echo 'Password is ${SERVER_CRED_PSW}'"
                }
            }
        }

        stage("Deploy") {
            steps {
                sh "echo 'Deployed'"
            }
        }
    }
}
