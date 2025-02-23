import boto3

s3_client = boto3.client("s3", region_name="us-east-1")
S3_BUCKET = "1225969188-in-bucket"

def count_s3_objects(bucket_name):
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        print(len(response.get("Contents", [])))
    except Exception as e:
        print(f"Error: {str(e)}")

count_s3_objects(S3_BUCKET)
