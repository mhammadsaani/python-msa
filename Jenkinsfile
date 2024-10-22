pipeline{
    agent any
    environment {
        USERNAME = "Hammad"
        PASSWORD = "Test123"
    }
    stages{
        stage("username") {
        steps {
            sh " echo 'username is ${USERNAME} "
        }
        }

        stage("password"){
            steps{
                sh "echo 'Password is ${PASSWORD}'"
            }
        }

        stage("Deploy"){
            steps{
                sh "echo 'Deployed'"
            }
        }
    }
}