@Library('my-shared-library') _  // Load shared library

pipeline {
    agent { label 'yoda' }  // Run on agent "yoda"

    parameters {
        string(name: 'NEW_TITLE', defaultValue: 'Welcome to My Site', description: 'Enter the new title')
    }

    stages {
        stage('Wait for User Input') {
            steps {
                script {
                    def userInput = input(
                        message: 'Enter a new title before proceeding:',
                        parameters: [
                            string(name: 'NEW_TITLE', defaultValue: 'Welcome', description: 'Enter the new title')
                        ]
                    )
                    env.USER_TITLE = userInput  // Store input as environment variable
                }
            }
        }

        stage('Get Build Metadata') {
            steps {
                script {
                    def metadata = buildInfo.getMetadata(currentBuild)
                    env.BUILD_NUMBER = metadata.buildNumber
                    env.DURATION = metadata.duration
                    env.PIPELINE_NAME = metadata.pipelineName
                }
            }
        }

        stage('Update HTML') {
            steps {
                script {
                    sh """
                    python3 /mnt/d/Devops/Project/update_html.py "${env.USER_TITLE}" "${env.BUILD_NUMBER}" "${env.PIPELINE_NAME}" "${env.DURATION}"
                    """
                }
            }
        }
    }
}
