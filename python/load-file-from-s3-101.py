

import boto3
import botocore

BUCKET_NAME = 'poc-101-s3'
BUCKET_FILE_NAME = 'scripts/create-schema-and-initialize.sql'
LOCAL_FILE_NAME = "db.sql"
# OBJECT_NAME = "scripts/create-schema-and-initialize.sql"


"""
Links:
01: https://devqa.io/download-s3-objects-python-boto3/ 
"""
def download_s3_file():
    s3 = boto3.client('s3')
    s3.download_file(BUCKET_NAME, BUCKET_FILE_NAME, LOCAL_FILE_NAME)


"""
LinK:
01: https://www.learnaws.org/2021/02/24/boto3-resource-client/
02: https://www.radishlogic.com/aws/s3/how-to-download-files-from-s3-bucket-using-boto3-and-python/ 

"""
def download_s3_file01():
    s3 = boto3.resource('s3')

    obj = s3.Object(
        bucket_name=BUCKET_NAME,
        key=BUCKET_FILE_NAME
    )

    with open('./python/temp/db01.sql', 'wb') as file:
        
        obj.download_fileobj(
            Fileobj=file
        )



def downlaod_s3_file02():
    try:
        s3 = boto3.resource('s3')
        s3.Bucket(BUCKET_NAME).download_file(BUCKET_FILE_NAME, './python/temp/db02.sql')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

    
# download_s3_file()
# download_s3_file01()
downlaod_s3_file02()