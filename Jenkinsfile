pipeline {
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