
#### Use Case : Hosting a Website

    - List of WebServers :
        To Hosting a Website, We need to use webservers: i.e. Apache httpd, Apache2, Nginx, IIS etc...
            
    - Host A Website on Linux Distributions :
        - Ubuntu / Amazon Linux 

    - Host A Website on Windows:
        - IIS  

#### What is Package Management?
        - Search a Package 
        - Install a Package
        - Update the package index
        - Upgrade packages
        - Remove a Package
        
    - Package management :
        # AmazonLinux / CentOS / Fedora / RHEL : 
            $ rpm 
            $ yum 
        # https://www.redhat.com/sysadmin/how-manage-packages

        # Debian / Ubuntu :
            $ dpkg
            $ apt       [For Interactive Terminal]
            $ apt-get   [For Scripts]

        # https://ubuntu.com/server/docs/package-management

#### Search a Software is installed or not 
    - $ dpkg -l | grep apache2        --> Debian / Ubuntu
    - $ yum list installed | grep httpd --> AmazonLinux / CentOS / Fedora / RHEL

#### Package Management
    - $ yum install httpd -y

    - $ apt update              --> Debian / Ubuntu
    - $ apt install apache2 -y  --> Debian / Ubuntu

#### Documentation :
    - Path : /usr/share/man/man1/httpd.1.gz

    - Path : /usr/share/man/man8/apache2.8.gz --> Debian / Ubuntu

#### Configuration :
    - Path : /etc/httpd
    
    - Path : /etc/apache2 --> Debian / Ubuntu

#### Binary Files:
    - Path : /usr/sbin/httpd

    - Path : /usr/sbin/apache2 --> Debian / Ubuntu

#### DocumentRoot:
    - Path : /var/www/html/

#### Log Files :
    - Path : /var/log/httpd/

    - Path : /var/log/apache2/ --> Debian / Ubuntu

#### Controlling Services & Daemons : 
    
    - Service :

        Path : /usr/lib/systemd/system/httpd.service

        Path : /lib/systemd/system/apache2.service --> Debian / Ubuntu
    
    - To Enable a Service at boot level:
        $ systemctl enable httpd
        $ systemctl enable apache2 --> Debian / Ubuntu
    
    - To check a Service status:
        $ systemctl status httpd
        $ systemctl status apache2  --> Debian / Ubuntu

    - To Start a Service:
        $ systemctl start httpd
        $ systemctl start apache2 --> Debian / Ubuntu

    - To Restart a Service:
    
        $ systemctl restart httpd    

        $ systemctl start apache2  --> Debian / Ubuntu

        $ netstat -tulpn | grep LISTEN

        $ cat /etc/services | grep -w '80/tcp'

    - Take Public Ip and Go to Browser and paste:

        http://23.22.33.211/
    