pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.7-slim-buster'
                }
            }
            steps {
                sh 'python -m py_compile sources/extract_flashes.py'
            }
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'py.test --verbose --junit-xml test-reports/results.xml tests/test_extract_flashes.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        }
    }
}