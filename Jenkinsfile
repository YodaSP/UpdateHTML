@Library('my-shared-library') _  // Load shared library

pipeline {
    agent { label 'yoda' }  // Run on agent "yoda"

    stages {
        stage('Test Shared Library') {
            steps {
                script {
                    def metadata = buildInfo.getMetadata(currentBuild)
                    echo "Build Number: ${metadata.buildNumber}"
                    echo "Build Duration: ${metadata.duration}"
                    echo "Pipeline Name: ${metadata.pipelineName}"
                }
            }
        }
    }
}
