@Library('my-shared-library') _  // Load shared library

pipeline {
    agent { label 'yoda' }  // Run on agent "yoda"
    parameters {
     string(name: 'NEW_TITLE', defaultValue: 'Welcome to My Site', description: 'New Title for index.html')
    }
    stages {
        stage('Checkout Code') {
            steps {
                script {
                    checkout scm  // Uses the configured repository
                }
            }
        }
        
        stage('Test Checkout') {
            steps {
                script {
                    sh "ls -l"  // List files to verify checkout
                }
            }
        }

        stage('Invoke Python Script') {
            steps {
                script {
                    
                        sh "python3 ${WORKSPACE}/update_html.py '${params.NEW_TITLE}'"
                  
                }
            }
        }   

        stage('Jenkins Library Test') {
            steps {
                script {
                    def metadata = buildinfo.getMetadata(currentBuild)
                    echo "Build Metadata: ${metadata}"
                }
            }
        }
    }
}
