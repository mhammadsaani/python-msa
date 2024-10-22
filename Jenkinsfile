pipeline{
    agent any
    environment {
        SERVER_CRED = credentials('cred')
    }
    stages{
        stage("Parallel"){
            parallel{
                stage("username") {
                    steps {
                        sh " echo 'username is ${SERVER_CRED_USR}' "
                    }
                }
                stage("password"){
                    steps{
                        sh "echo 'Password is ${SERVER_CRED_PSW}'"
                    }
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