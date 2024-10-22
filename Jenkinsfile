pipeline{
    agent any
    stages{
        stage("Setup") {
        steps {
            sh " echo 'Setup Done' "
        }
        }

        stage("Test"){
            steps{
                sh "echo 'Hello'"
            }
        }

        stage("Deploy"){
            steps{
                sh "echo 'Deployed'"
            }
        }
    }
}