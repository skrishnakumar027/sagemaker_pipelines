import boto3
import os

def create_session(role_arn=None, role_session_name='jenkins_session'):
    if role_arn:
        sts_client = session.client('sts')
        
        # Assume the role in the external account
        response = sts_client.assume_role(RoleArn=role_arn,RoleSessionName=role_session_name)
        
        # Extract the temporary credentials from the response
        credentials = response['Credentials']
        
        # Create a new session using the temporary credentials
        session = boto3.Session(
            aws_access_key_id=credentials['AccessKeyId'],
            aws_secret_access_key=credentials['SecretAccessKey'],
            aws_session_token=credentials['SessionToken']
        )
        
        return session
    else:
        return boto3.Session()
        
def main():
    Account_ID = os.environ['Account_ID']
    Region = os.environ['Region']
    Role_name = os.environ['Role_name']

    role_arn = 'arn:aws:iam::' + str(Account_ID) + ':role/' + str(Role_name)
    role_session_name = 'SESSION_NAME'

    session = create_session(role_arn, role_session_name)
    
    # Create an S3 client using the session
    s3_client = session.client('s3')

    # List all buckets
    response = s3_client.list_buckets()

    # Extract bucket names from the response
    bucket_names = [bucket['Name'] for bucket in response['Buckets']]

    # Print bucket names
    for bucket_name in bucket_names:
        print(bucket_name)

if __name__=='__main__':
    main()
