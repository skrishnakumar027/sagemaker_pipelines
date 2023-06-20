import boto3

# Create a session using the AWS credentials from Jenkins environment variables
session = boto3.Session(
    aws_access_key_id='ASIAVV73ELQ7JLSDUHWL',
    aws_secret_access_key='rOBGTmlgB2LCL7/rl6t9US43jjq4L6Rn+OK/hix3',
    aws_session_token='IQoJb3JpZ2luX2VjEFEaCXVzLWVhc3QtMiJIMEYCIQC4h27SZruMHD8K3wnLtVa7yq1Rl5s7WicJO0b1tTUfgAIhALbpAQg7M0cCMAsraLSpjgxNXIiP6GaCVfdLCUMZ5VZgKooDCKr//////////wEQARoMMzkwODMxODIzOTM0IgxiLgxAiE8MBcP4sSEq3gI1MhcB3QtnF2GLTyaUBuPJrQuR9o7Izy7ML4uW324Pkj3iFD+RfrHeb/SuZnG81xrdlSMw9K6V4+w4qThyYsckOMaWzq60vOBE0j/mNW8ZyA3ClvKFPrpFjN6F/CDjeZAbIfMJcEpM2cB22PpTVrA047+b+PMAJP0AgKqO2O+FcXPHb9nRZ5VgBujQJPXKPoXHI5c1QmHTFyOckEFmdVtCrhvSqx4h4+ZiKnMHCT0Xoiv4oUhsR5QHnBW4a3uaX4AK7cRnG4D5UEYXVBWDerEEquHgVbFefs+K9qgqRXThpzB+fCqdHQfBEJCUblnxidHIMGibDv+yUC692KoL3g5RcLmgZ+2OXmnYWcWptPbKM9Q0XEqbm677HedqMH40Z3/FempyjBa9YC+is0cUSF/AqW6WhvQIaFTov5ZbC9CUBBr7wjPNnlHQK4qQXazJ4xFclK/f739mFKdx6vYUDTDHv8ekBjqlAaIPK2eSgyyZjH2vRyyvgSZ6+eEJr2ImP1rWcx5sCIecTs1/Dl6xRw8dqYN75V3vgrA+JpRWgTqA51WYDP1jvWABjQJSz6nDGNDKtFJaa6Pla74QOWxOoWtINlgbRMFJjYtvNy8gmPNIj1OcWcSpDRVBPfy4Fg7hU7u9fyMUBDJmpCIJHVpdlBhQ7SuCab7sNCffbGEUw+l1ScIMSR/IVU1pAuWLpA=='
)

# Use the session to interact with AWS services
# s3_client = session.client('s3')
# print(s3_client.list_buckets())

sagemaker_client = session.client('sagemaker', region_name='us-east-2')

# Define the pipeline definition file location
pipeline_definition_file = 'pipeline_definition.json'

# Read the pipeline definition file
with open(pipeline_definition_file, 'r') as f:
    pipeline_definition = f.read()

# Create the pipeline
response = sagemaker_client.create_pipeline(
    PipelineName='MyPipeline_jenkins',
    PipelineDefinition=pipeline_definition,
    RoleArn='arn:aws:iam::390831823934:role/team-role-dep-aiml-sagemaker-execution',
    Tags=[
        {
            'Key': 'Key1',
            'Value': 'Value1'
        },
        {
            'Key': 'Key2',
            'Value': 'Value2'
        }
    ]
)

# Get the ARN of the created pipeline
pipeline_arn = response['PipelineArn']

print('SageMaker pipeline created with ARN:', pipeline_arn)
