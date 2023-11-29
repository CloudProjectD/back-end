import boto3
from boto3.dynamodb.conditions import Attr
from botocore.exceptions import ClientError
from fastapi import UploadFile
from app.core.config import settings
from typing import List
from app.models.domain.messages import Message


def get_aws_client(service_name: str):
    return boto3.client(
        service_name,
        region_name=settings.AWS_REGION,
        aws_access_key_id=settings.AWS_ACCESS_KEY,
        aws_secret_access_key=settings.AWS_SECRET_KEY,
        aws_session_token=settings.AWS_SESSION_TOKEN,
    )


def s3_upload(
    files: List[UploadFile], post_id: int, user_email: str, category: str
) -> bool:
    client = get_aws_client("s3")
    try:
        for file in files:
            new_filename = f"{user_email}/{category}/{post_id}/{file.filename}"
            client.upload_fileobj(
                file.file,
                settings.BUCKET_NAME,
                new_filename,
                ExtraArgs={"ContentType": file.content_type},
            )
    except ClientError as e:
        return False
    return True


def s3_get(post_id: int, user_email: str, category: str) -> List[UploadFile]:
    client = get_aws_client("s3")
    try:
        res = client.list_objects(
            Bucket=settings.BUCKET_NAME, Prefix=f"{user_email}/{category}/{post_id}/"
        )
        file_list = []
        for file_detail in res["Contents"]:
            image_url = f'https://{settings.BUCKET_NAME}.s3.{settings.AWS_REGION}.amazonaws.com/{file_detail["Key"]}'
            file_list.append(image_url)
        return file_list
    except ClientError as e:
        return []


class DynamoDBHandler:
    def __init__(self):
        self.client = get_aws_client("dynamodb")
        self.table_name = settings.DYNAMODB_TABLE_NAME
        self.table = self.get_table()

    def get_table(self):
        dynamodb = boto3.resource(
            "dynamodb",
            region_name="us-east-1",
            aws_access_key_id=settings.AWS_ACCESS_KEY,
            aws_secret_access_key=settings.AWS_SECRET_KEY,
            aws_session_token=settings.AWS_SESSION_TOKEN,
        )
        return dynamodb.Table(self.table_name)

    def put_object(self, message: Message):
        try:
            self.table.put_item(
                Item={
                    "id": message.id,
                    "post_id": message.post_id,
                    "created_at": message.created_at.isoformat(),
                    "category": message.category,
                    "sender": message.sender,
                    "recipient": message.recipient,
                    "content": message.content,
                }
            )
        except ClientError as err:
            print(err)
            return False
        return True

    def get_all_user_objects(self, user_id: int):
        try:
            response = self.table.scan(
                FilterExpression=Attr("sender").eq(user_id)
                | Attr("recipient").eq(user_id)
            )
        except ClientError as err:
            print(err)
            return False
        else:
            items = response.get("Items", [])
        return items

    def get_user_post_objects(self, user_id: int, post_id: int):
        try:
            response = self.table.scan(
                FilterExpression=(
                    Attr("sender").eq(user_id) | Attr("recipient").eq(user_id)
                )
                & Attr("post_id").eq(post_id)
            )
        except ClientError as err:
            print(err)
            return False
        else:
            items = response.get("Items", [])
        return items
