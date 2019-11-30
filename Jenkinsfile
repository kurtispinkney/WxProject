

        stage('Deliver') {
            agent {
                docker {
                    image 'cdrx/pyinstaller-linux:python2'
                }
            }
            steps {
                sh 'pyinstaller --onefile sources/add2vals.py'
            }
            post {
                success {
                    archiveArtifacts 'dist/add2vals'
                }
            }
        }

and add a skipStagesAfterUnstable option so that you end up with:

pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.7-slim-buster'
                }
            }
            steps {
                sh 'python -m py_compile src/extract_flashes.py'
            }
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