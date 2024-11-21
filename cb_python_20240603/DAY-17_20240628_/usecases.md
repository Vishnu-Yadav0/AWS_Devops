# Session Video:

```
https://drive.google.com/file/d/1ZgLvrpAZV6FSPVBXYiNJ0Xm0SmEkfo_D/view?usp=sharing
```

#### Python Web frameworks

```

Example Architecture

Here's how the architecture might look:

S3: Hosts static and media files.
EC2/ECS: Runs the Django application.
RDS: Manages the database.
ELB: Load balances the traffic to your application.
Route 53: Manages DNS.
ACM: Handles SSL certificates.
CodePipeline: Automates the deployment process.

AWS Lambda with API Gateway: You can deploy Django as a serverless application using AWS Lambda and API Gateway. 

This method requires some adaptation, often involving using the Zappa or Chalice frameworks to package and deploy the Django app.


https://fastapi.tiangolo.com/

https://flask.palletsprojects.com/en/3.0.x/

https://docs.djangoproject.com/en/5.0/intro/tutorial01/

https://docs.djangoproject.com/en/5.0/intro/tutorial02/
```

