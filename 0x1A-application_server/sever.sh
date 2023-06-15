#!/usr/bin/env bash
#configures anew server to return a custom header

sudo apt-get -y update
sudo apt-get -y install nginx
echo "Hello world" | sudo tee /var/www/html/index.nginx-debian.html
str="\\\tadd_header X-Served-By $HOSTNAME;"

sudo sed -i "36i $str" /etc/nginx/sites-available/default
sudo service nginx restart