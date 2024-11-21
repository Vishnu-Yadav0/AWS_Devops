#### Session Video

```
https://drive.google.com/file/d/1bfBhCVcn6ihffUY2XYBXni_3Ah6iuK3f/view?usp=sharing
```

#### Storage - S3 - EBS - EFS 

#### https://aws.amazon.com/efs/

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "S3FullAccess",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam:::user/svc-c3ops"
            },
            "Action": "s3:*",
            "Resource": "arn:aws:s3:::"
        }
    ]
}

```


