pipeline{
    agent any
    stage("Setup") {
        steps {
            sh "pip install -r requirements.txt"
        }
    }

    stage("Test"){
        steps{
            sh "echo 'Hello'"
        }
    }
}