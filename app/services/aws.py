import boto3
import logging
from botocore.exceptions import ClientError
from fastapi import UploadFile
from app.core.config import settings
from typing import List
from app.models.domain.messages import Message

def get_aws_client(service_name: str):
    return boto3.client(
        service_name,
        region_name="us-east-1",
        aws_access_key_id=settings.AWS_ACCESS_KEY,
        aws_secret_access_key=settings.AWS_SECRET_KEY,
        aws_session_token=settings.AWS_SESSION_TOKEN,
    )

def s3_upload(files: List[UploadFile], post_id: int, user_email: str, category: str) -> bool:
    client = get_aws_client('s3')
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

class DynamoDBHandler:
    def __init__(self):
        self.client = get_aws_client('dynamodb')
        self.table_name = settings.DYNAMODB_TABLE_NAME
        self.table = self.get_table()

    def get_table(self):
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        return dynamodb.Table(self.table_name)

    def create_table(self):
        try:
            self.client.create_table(
                TableName=self.table_name,
                KeySchema=[
                    {'AttributeName': 'user_id', 'KeyType': 'HASH'},
                    {'AttributeName': 'created_at', 'KeyType': 'RANGE'}
                ],
                AttributeDefinitions=[
                    {'AttributeName': 'user_id', 'AttributeType': 'N'},
                    {'AttributeName': 'created_at', 'AttributeType': 'S'}
                ],
                ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
            )
        except ClientError as e:
            return False
        return True

    def put_object(self, message: Message):
        try:
            self.table.put_item(
                Item={
                    'user_id': message.user_id,
                    'post_id': message.post_id,
                    'created_at': message.created_at.isoformat(),
                    'category': message.category,
                    'sender': message.sender_id,
                    'recipient': message.recipient_id,
                    'content': message.content,
                }
            )
        except ClientError as e:
            return False
        return True
    
    def get_object(self, user_id: int, created_at: str):
        try:
            response = self.table.get_item(Key={'user_id':user_id, 'created_at':created_at})
        except ClientError as err:
            logging.error(
                "Couldn't get message from table %s.", self.table_name)
            raise
        else:
            return response['Item']