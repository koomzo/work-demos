import boto3

FILE_NAME = "db.sql"
BUCKET_NAME = "poc-101-s3"
OBJECT_NAME = "scripts/create-schema-and-initialize.sql"

session = boto3.Session(profile_name='sandbox')

# s3_object = session.Object(
#     bucket_name=BUCKET_NAME,
#     key='s3_folder/photo.jpg'
# )

# s3_object.download_file(Filename='local_folder/image.jpg')

client = session.client('s3', region_name='us-east-1')
client.list_buckets()

with open('FILE_NAME', 'wb') as f:
    client.download_fileobj('BUCKET_NAME', 'OBJECT_NAME', f)
# Upload the Python script to the S3 bucket



# sts = session.client('sts')
# print(sts.get_caller_identity())

# sts = boto3.client('sts')
# print(sts.get_caller_identity())
