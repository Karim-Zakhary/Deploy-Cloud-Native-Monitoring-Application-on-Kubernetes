import boto3

ecr_client = boto3.client('ecr')

repositry_name = "my-cloud-native-repo"

response = ecr_client.create_repository(repositoryName=repositry_name)


repositry_uri = response['repository']['repositoryUri']
print(repositry_uri) 

