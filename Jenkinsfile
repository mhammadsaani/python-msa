pipeline{
    agent any
    environment {
        SERVER_CRED = credentials('cred')
    }
    stages{
        stage("Parallel"){
stage("username") {
        steps {
            sh " echo 'username is ${SERVER_CRED_USR}' "
        }
        }

        stage("password"){
            steps{
                sh "echo 'Password is ${SERVER_CRED_PAS}'"
            }
        }
        }
        

        stage("Deploy"){
            steps{
                sh "echo 'Deployed'"
            }
        }
    }
}