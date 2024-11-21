#!/bin/bash

# Setup Hostname
sudo hostnamectl set-hostname "tomcat.c3ops.io"

# Update the hostname part of Host File
echo "`hostname -I | awk '{ print $1 }'` `hostname`" >> /etc/hosts

# Update Ubuntu Repository
sudo apt-get update

# Download, & Install Utility Softwares
sudo apt-get install git wget unzip curl tree -y

# Download, Install Java 17
sudo apt-get install openjdk-17-jdk -y

# Backup the Environment File
sudo cp -pvr /etc/environment "/etc/environment_$(date +%F_%R)"

# Create Environment Variables
echo "JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64/" >> /etc/environment

# Go to /opt directory to download Apache Tomcat 
cd /opt/

# Download Apache Tomcat - Application
sudo wget https://downloads.apache.org/tomcat/tomcat-8/v8.5.100/bin/apache-tomcat-8.5.100.tar.gz

# Extract the Tomcat File
sudo tar xvzf apache-tomcat-8.5.100.tar.gz

# Rename the Tomcat Folder
sudo mv apache-tomcat-8.5.100 tomcat

# Go Inside the Tomcat Folder
cd /opt/tomcat/

# Take Tomcat Configuration as backup 
sudo cp -pvr /opt/tomcat/conf/tomcat-users.xml "/opt/tomcat/conf/tomcat-users.xml_$(date +%F_%R)"

# To delete last line and which contains </tomcat-users>
sed -i '$d' /opt/tomcat/conf/tomcat-users.xml

#Add User & Attach Roles to Tomcat 
echo '<role rolename="manager-gui"/>'  >> /opt/tomcat/conf/tomcat-users.xml
echo '<role rolename="manager-script"/>' >> /opt/tomcat/conf/tomcat-users.xml
echo '<role rolename="manager-jmx"/>'    >> /opt/tomcat/conf/tomcat-users.xml
echo '<role rolename="manager-status"/>' >> /opt/tomcat/conf/tomcat-users.xml
echo '<role rolename="admin-gui"/>'     >> /opt/tomcat/conf/tomcat-users.xml
echo '<role rolename="admin-script"/>' >> /opt/tomcat/conf/tomcat-users.xml
echo '<user username="admin" password="redhat@123" roles="manager-gui,manager-script,manager-jmx,manager-status,admin-gui,admin-script"/>' >> /opt/tomcat/conf/tomcat-users.xml
echo "</tomcat-users>" >> /opt/tomcat/conf/tomcat-users.xml

echo '<?xml version="1.0" encoding="UTF-8"?>' > /opt/tomcat/webapps/manager/META-INF/context.xml
echo '<Context antiResourceLocking="false" privileged="true"' >> /opt/tomcat/webapps/manager/META-INF/context.xml
echo '</Context>' >> /opt/tomcat/webapps/manager/META-INF/context.xml

echo '<?xml version="1.0" encoding="UTF-8"?>' > /opt/tomcat/webapps/host-manager/META-INF/context.xml
echo '<Context antiResourceLocking="false" privileged="true"' >> /opt/tomcat/webapps/host-manager/META-INF/context.xml
echo '</Context>' >> /opt/tomcat/webapps/host-manager/META-INF/context.xml

echo '[Unit]' > /etc/systemd/system/tomcat.service
echo 'Description=Apache Tomcat Web Application Container' >> /etc/systemd/system/tomcat.service
echo 'After=network.target' >> /etc/systemd/system/tomcat.service

echo '[Service]' >> /etc/systemd/system/tomcat.service
echo 'Type=forking' >> /etc/systemd/system/tomcat.service

echo 'Environment=JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64/' >> /etc/systemd/system/tomcat.service
echo 'Environment=CATALINA_PID=/opt/tomcat/temp/tomcat.pid' >> /etc/systemd/system/tomcat.service
echo 'Environment=CATALINA_HOME=/opt/tomcat' >> /etc/systemd/system/tomcat.service
echo 'Environment=CATALINA_BASE=/opt/tomcat' >> /etc/systemd/system/tomcat.service
echo 'Environment='CATALINA_OPTS=-Xms512M -Xmx1024M -server -XX:+UseParallelGC'' >> /etc/systemd/system/tomcat.service
echo 'Environment='JAVA_OPTS=-Djava.awt.headless=true -Djava.security.egd=file:/dev/./urandom'' >> /etc/systemd/system/tomcat.service

echo 'ExecStart=/opt/tomcat/bin/startup.sh' >> /etc/systemd/system/tomcat.service
echo 'ExecStop=/opt/tomcat/bin/shutdown.sh' >> /etc/systemd/system/tomcat.service

echo 'User=root' >> /etc/systemd/system/tomcat.service
echo 'Group=root' >> /etc/systemd/system/tomcat.service
echo 'UMask=0007' >> /etc/systemd/system/tomcat.service
echo 'RestartSec=10' >> /etc/systemd/system/tomcat.service
echo 'Restart=always' >> /etc/systemd/system/tomcat.service

echo '[Install]' >> /etc/systemd/system/tomcat.service
echo 'WantedBy=multi-user.target' >> /etc/systemd/system/tomcat.service

systemctl daemon-reload
systemctl enable tomcat
systemctl restart tomcat

wget https://gitlab.com/kesav.kummari/ansible-role-tomcat/-/raw/main/tomcat/files/devops.war /opt/tomcat/webapps/

systemctl restart tomcat

# Open a Browser and access tomcat : http://public_ip_of_ec2_instance:port(8080)
