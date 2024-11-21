#### Session Video

```
https://drive.google.com/file/d/1HEltB7QbXArN6V6t7F8Fj92aYaqMq291/view?usp=sharing
```

#### Storage - S3 - CloudFront 


```
Use Case-1 : Connect and pull S3 Objects to EC2 instance 



# Synopsis:
aws s3 <Command> [<Arg> ...]

# Available Commands:
cp
ls
mb
mv
presign
rb
rm
sync
website

aws s3 cp /tmp/foo/ s3://bucket/ --recursive --exclude "*" --include "*.jpg"

If you wanted to include both .jpg files as well as .txt files you can run:

aws s3 cp /tmp/foo/ s3://bucket/ --recursive --exclude "*" --include "*.jpg" --include "*.txt"


# File : Shell Script i.e. sync_s3.sh

#!/bin/bash

# Variables
S3_BUCKET="s3://dev.c3ops.io"
LOCAL_DIR="/var/www/html/"

# Sync S3 bucket to local directory
aws s3 sync $S3_BUCKET $LOCAL_DIR

# Sync local directory back to S3 bucket
aws s3 sync $LOCAL_DIR $S3_BUCKET

# Log the operation
echo "$(date): Sync completed." >> /var/log/s3_sync.log


# Make the script executable:
chmod +x /opt/sync_s3.sh


# Crontab 
crontab -e
*/5 * * * * /opt/sync_s3.sh >> /var/log/s3_sync_crontab.log


sudo yum install cronie -y
rpm -ql cronie
systemctl status crond.service
systemctl enable crond.service
systemctl start crond.service

crontab -l
crontab -e
*/5 * * * * /opt/sync_s3.sh >> /var/log/s3_sync_crontab.log

#  Use Case with Commands :

[root@web opt]# ls -lrt
drwxr-xr-x. 4 root root  33 May 24 08:35 aws
-rwxr-xr-x. 1 root root 306 Jun 27 09:46 sync_s3.sh

[root@web opt]# crontab -l
#
*/5 * * * * /opt/sync_s3.sh >> /var/log/s3_sync_crontab.log

[root@web opt]# date
Thu Jun 27 09:55:55 IST 2024

[root@web opt]# ls -lrt /var/log/s3_sync_crontab.log
-rw-r--r--. 1 root root 136 Jun 27 09:55 /var/log/s3_sync_crontab.log

[root@web opt]# ls -lrt /var/log/s3_sync.log
-rw-r--r--. 1 root root 46 Jun 27 09:55 /var/log/s3_sync.log


```

#### Policies

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


