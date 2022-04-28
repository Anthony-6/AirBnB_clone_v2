#!/usr/bin/env bash
# comment
apt-get -y update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
mkdir -p /data/webstatic/releases/test/
mkdir -p /data/webstatic/shared/
echo "Holberton School" > /data/web_static/releases/test/index.html
ls -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i 'location /hbnb_static { alias /data/web_static/current/; }' /etc/nginx/sites-available/default
service nginx restart
