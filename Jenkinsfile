pipeline {
    agent any
    stages {
      stage('version') {
        steps {
          sh 'python3 --version'
        }
      }
      stage('Hello') {
        steps {
          sh 'python3 sagemaker_pipeline.py'
        }
      }
    }
}