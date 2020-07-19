Jenkinsfile
pipeline {
  agent { docker { image 'python:3.7.2' } }
    stages {
        stage('build') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('test') {
            steps {
                sh './run_tests.sh'
            }   
        }
    }
}