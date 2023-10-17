import boto3
from botocore.exceptions import ClientError
from fastapi import UploadFile
from app.core.config import settings
from typing import List


def s3_upload(files: List[UploadFile], post_id: int, user_email: str) -> bool:
    client = boto3.client(
        "s3",
        region_name="us-east-1",
        aws_access_key_id=settings.AWS_ACCESS_KEY,
        aws_secret_access_key=settings.AWS_SECRET_KEY,
    )
    try:
        for file in files:
            new_filename = f"/{user_email}/{post_id}/{file.filename}"
            client.upload_fileobj(
                file.file,
                settings.BUCKET_NAME,
                new_filename,
                ExtraArgs={"ContentType": file.content_type},
            )
    except ClientError as e:
        return False
    return True
