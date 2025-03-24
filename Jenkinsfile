@Library('my-shared-library') _  // Load shared library

pipeline {
    agent { label 'yoda' }  // Run on agent "yoda"

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
    }
}
