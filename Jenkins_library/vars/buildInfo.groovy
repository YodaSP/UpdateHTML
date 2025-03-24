def getMetadata(currentBuild) {
    return [
        buildNumber: currentBuild.number,
        duration: currentBuild.durationString.replace(' and counting', ''),
        pipelineName: env.JOB_NAME
    ]
}
