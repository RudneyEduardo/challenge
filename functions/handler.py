# coding=utf-8


import json
from urllib import response
import urllib.parse
import boto3
from boto3.dynamodb.conditions import Key, Attr
import io
s3 = boto3.client('s3')


dynamodb = boto3.client('dynamodb')


def extractMetadata(event, context):
    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(
        event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print("BUCKET:" + bucket)
        print("KEY: " + key)
        contentType = response['ContentType']
        contentLength = str(response['ContentLength'])
        # Put image metadata in dynamodb
        s3Obj = { 'Bucket': bucket, 'Key': key }
        jsons3Obj = json.dumps(s3Obj)
        dynamodb.put_item(TableName='desafio-aws-dev-images', Item={'s3objectkey': {'S': jsons3Obj},
                                                                    'ContentType': {'S': contentType},
                                                                    'ContentLength': {'S': contentLength}
                                                                    })
        return 'Inserted Item!'
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e


def getMetadata(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(
        event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        s3Obj = { 'Bucket': bucket, 'Key': key }
        jsons3Obj = json.dumps(s3Obj)
        
        resp = dynamodb.get_item(TableName='desafio-aws-dev-images', Key={"s3objectkey": jsons3Obj})
        ContentType = resp['Item']['ContentType']
        ContentLength = resp['Item']['ContentLength']
        return {ContentType:ContentType, ContentLength:ContentLength}
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e


def getImage(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(
        event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        s3.Bucket(bucket).download_file(key, 'download.jpg')
    except boto3.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

def infoImages(event, images):
    table = dynamodb.Table('desafio-aws-dev-images')
    paginator = dynamodb.get_paginator("scan")

    for page in paginator.paginate(TableName=table):
        yield from page["Items"]

    