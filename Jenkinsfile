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
          sh 'pip3 install boto3 && python3 sagemaker_pipeline.py'
        }
      }
    }
}
