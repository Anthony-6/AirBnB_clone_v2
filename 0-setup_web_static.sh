#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
mkdir -p /data/webstatic/releases/test/
mkdir -p /data/webstatic/shared/
echo "Simple content to test nginx configuration" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i 'location /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default
sudo service nginx restart
