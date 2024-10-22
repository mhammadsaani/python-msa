pipeline{
    agent any
    stages{
        stage("Setup") {
        steps {
            sh "pip install -r requirements.txt --break-system-packages"
        }
        }

        stage("Test"){
            steps{
                sh "echo 'Hello'"
            }
        }
    }
}