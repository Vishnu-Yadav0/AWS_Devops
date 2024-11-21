#### Session Video

```
https://drive.google.com/file/d/1c6EyX7eU0nIF8Zrly5UBB9i_Qsc_ayb2/view?usp=sharing
```

#### Storage - S3 - EBS - EFS 

#### https://aws.amazon.com/efs/

```

# User Data 

#!/bin/bash

# To Install Web Server 
yum install httpd -y 

# Enable Webserver Deamon at Boot Level & Start the Service 
systemctl enable httpd
systemctl start httpd

# Deploy Simple Code 
echo "<h1><center>Welcome To Cloud Binary - $(hostname -f)</center></h1>" > /var/www/html/index.html

sudo yum install -y amazon-efs-utils

# https://docs.aws.amazon.com/efs/latest/ug/installing-amazon-efs-utils.html#installing-other-distro
# sudo apt-get update 
# sudo apt-get install git curl wget unzip -y 
# sudo apt-get -y install git binutils ### For Ubuntu
# git clone https://github.com/aws/efs-utils
# root@ip-172-31-22-231:~/efs-utils# pwd
# /root/efs-utils
# root@ip-172-31-22-231:~/efs-utils# ls -lrt build-deb.sh
# -rwxr-xr-x 1 root root 2449 May 18 05:18 build-deb.sh
# root@ip-172-31-22-231:~/efs-utils# ./build-deb.sh
# sudo apt-get -y install ./build/amazon-efs-utils*deb
# systemctl status rpcbind.service


sudo service nfs start
sudo service nfs status

EFS DNS : fs-0a56f06fb1447664d.efs.us-east-1.amazonaws.com

sudo mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport <efs_dns_name>:/ /efs-mount-point

#sudo mkdir /efs-mount-point

sudo mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-0a56f06fb1447664d.efs.us-east-1.amazonaws.com:/ /var/www/html/ 

echo "Welcome To EFS File System - Server-1" > /var/www/html/index.html


```



```
# Server-1:

#!/bin/bash

# Update Package Manager
sudo apt update
sudo apt-get install git curl wget unzip -y
sudo apt-get -y install binutils
cd /root/
git clone https://github.com/aws/efs-utils
cd /root/efs-utils
bash /root/efs-utils/build-deb.sh
sudo apt-get -y install ./build/amazon-efs-utils*deb

# To Install Web Server 
sudo apt install apache2 -y 

# Enable Webserver Deamon at Boot Level & Start the Service 
systemctl enable apache2
systemctl start apache2

# Deploy Simple Code 
# echo "<h1><center>Welcome To Cloud Binary - Learn By Doing - $(hostname -f)</center></h1>" > /var/www/html/index.html

sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-0e96bcbcf344da90b.efs.ap-south-1.amazonaws.com:/ /var/www/html/


```


#### Task:

```
Create EFS and Mount on AmazonLinux
Create EFS and Mount on Ubuntu
Create FsX and Mount on Windows

```