#### Session Video

```
https://drive.google.com/file/d/1mfpa3L5gR0bkjaLLNatvDlxImHhTFi2a/view?usp=sharing
```

#### Route53

```


#!/bin/bash

sudo apt-get update
sudo apt-get install apache2 -y 
sudo systemctl enable apache2
sudo systemctl start apache2
echo "<html><head><title>Server-1</title></head><body bgcolor="olive"><h1>Welcome To C3Ops - Server `hostname -I`</h1></html>" > /var/www/html/index.html


#!/bin/bash

sudo apt-get update
sudo apt-get install apache2 -y 
sudo systemctl enable apache2
sudo systemctl start apache2
echo "<html><head><title>Server-2</title></head><body bgcolor="white"><h1>Welcome To Cloud Binary - Server `hostname -I`</h1></html>" > /var/www/html/index.html


https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html
```

