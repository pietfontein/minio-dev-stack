#!/usr/bin/env python3
"""
MinIO Python SDK Example
"""
import boto3

def main():
    # Initialize MinIO client
    s3 = boto3.client('s3',
        endpoint_url='http://localhost:9000',
        aws_access_key_id='admin',
        aws_secret_access_key='password123',
        use_ssl=False
    )
    
    print("Ì∫Ä MinIO Python SDK Example")
    print("=" * 40)
    
    # List all buckets
    response = s3.list_buckets()
    print("Ì≥¶ Available buckets:")
    for bucket in response['Buckets']:
        print(f"   ‚Ä¢ {bucket['Name']}")
    
    # Example: Work with a test bucket
    test_bucket = "test-python-bucket"
    
    try:
        # Create bucket if it doesn't exist
        s3.create_bucket(Bucket=test_bucket)
        print(f"‚úÖ Created bucket: {test_bucket}")
    except Exception as e:
        print(f"‚ÑπÔ∏è  Bucket may already exist: {test_bucket}")
    
    # Upload a test file
    s3.put_object(
        Bucket=test_bucket,
        Key="hello_python.txt",
        Body=b"Hello from Python SDK!",
        ContentType="text/plain"
    )
    print("‚úÖ Uploaded test file")
    
    # List objects in the bucket
    objects = s3.list_objects_v2(Bucket=test_bucket)
    if 'Contents' in objects:
        print(f"Ì≥Å Files in {test_bucket}:")
        for obj in objects['Contents']:
            print(f"   ‚Ä¢ {obj['Key']} ({obj['Size']} bytes)")

if __name__ == "__main__":
    main()
