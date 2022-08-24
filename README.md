# serverless-challenge
Build a serverless architecture for image analysis 

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
foo@bar:~$ serverless deploy --stage dev
foo
```



