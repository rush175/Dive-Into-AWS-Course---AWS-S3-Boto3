# https://kirr.co/bnk7dx
import boto3

AWS_ACCESS_KEY_ID = 'AKIAIPCQFHKC4E4EZ62A' 
AWS_SECRET_ACCESS_KEY = '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'
AWS_DEFAULT_REGION = 'us-east-1'


client = boto3.client('s3',
	aws_access_key_id=AWS_ACCESS_KEY_ID,
	aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
	region_name=AWS_DEFAULT_REGION
	)


response = client.list_buckets()

print(response)