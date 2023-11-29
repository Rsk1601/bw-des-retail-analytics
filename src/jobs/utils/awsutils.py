# from vaultUtils import get_aws_access_keys

# def retrieve_aws_keys():
#     vault_url = "http://127.0.0.1:8200"
#     vault_token = "hvs.la3oPoRng7kzBSTPgkWfkRbK"
#     secret_path = 'secret/data/aws'

#     try:
#         access_key, secret_key = get_aws_access_keys(vault_url, vault_token, secret_path)
#         if access_key and secret_key:
#             print(f"Retrieved access_key: {access_key}")
#             print(f"Retrieved secret_key: {secret_key}")
#         else:
#             print("Secret not found or empty")
#     except (ValueError, ConnectionError, RuntimeError) as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     retrieve_aws_keys()
    

# import boto3
# class AWSConnector:
#     def __init__(self, aws_access_key, aws_secret_key, client='s3', region='us-east-1'):
#         self.aws_access_key = aws_access_key
#         self.aws_secret_key = aws_secret_key
#         self.region = region
#         self.aws_client = client
#         self.session = self.create_session()
#         self.aws_client_conn = self.create_aws_client()
        

#     def create_session(self):
#         """
#         Create an AWS session using the provided credentials and region.
#         """
#         session = boto3.Session(
#             aws_access_key_id=self.aws_access_key,
#             aws_secret_access_key=self.aws_secret_key,
#             region_name=self.region
#         )
#         return session

#     def create_aws_client(self):
#         """
#         Create an AWS client using the AWS session.
#         """
#         try:
#             aws_client_conn = self.session.client(self.aws_client)
#             return aws_client_conn
#         except Exception as e:
#             print(f"an error occured while creating aws client:{str(e)}")
#             return None
        
#     if __name__ == "__main__":
#           retrieve_aws_keys()

import boto3
from vaultUtils import get_aws_access_keys

class AWSConnector:
    def __init__(self, access_key, secret_key, region='us-east-1'):
        self.access_key = access_key
        self.secret_key = secret_key
        self.region = region

    def connect_to_aws(self):
        try:
            session = boto3.Session(
                aws_access_key_id=self.access_key,
                aws_secret_access_key=self.secret_key,
                region_name=self.region
            )
            return session
        except Exception as e:
            print(f"An error occurred while connecting to AWS: {str(e)}")
            return None

def retrieve_aws_keys():
    vault_url = "http://127.0.0.1:8200"
    vault_token = "hvs.la3oPoRng7kzBSTPgkWfkRbK"
    secret_path = 'secret/data/aws'

    try:
        access_key, secret_key = get_aws_access_keys(vault_url, vault_token, secret_path)
        if access_key and secret_key:
            print(f"Retrieved access_key: {access_key}")
            print(f"Retrieved secret_key: {secret_key}")

            # Create an instance of AWSConnector with retrieved keys
            aws_connector = AWSConnector(access_key, secret_key)

            # Establish connection to AWS
            aws_session = aws_connector.connect_to_aws()

            if aws_session:
                print("Successfully connected to AWS")
                # Use 'aws_session' for AWS operations here
                # For example, access S3 buckets, EC2 instances, etc.
            else:
                print("Failed to establish AWS connection")
        else:
            print("Secret not found or empty")
    except (ValueError, ConnectionError, RuntimeError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    retrieve_aws_keys()



    
    

        

            

    
