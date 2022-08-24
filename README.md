# serverless-challenge
Desafio para construir funções lambda em python usando Serverless Framework

# Functions 

- extractMetadata:
    Get S3ObjectKey and stores the image metadata in DynamoDb.

- getMetadata:
    Get S3ObjectKey and returns the image metadata.

- getImage:
    Get S3ObjectKey and downloads the image. 

- infoImages (not implemented fully):
    Return Db infos, such as the biggest size image, the smallest image size, the types of images stored in S3 and How much of each image type is saved.


# How to Run



```console
foo@bar:~$ npm install -g serverless
        (installs the serverless framework globally in your computer)
foo@bar:~$ serverless config credentials --provider aws --key (your amz account key) --secret  (your amz account secret key)
        (configure the AWS credentials in your computer)
foo@bar:~$ serverless deploy --stage dev
        (Now deploying the code)
```



