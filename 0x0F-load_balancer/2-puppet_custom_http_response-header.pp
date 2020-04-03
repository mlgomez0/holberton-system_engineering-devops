#creating a custom HTTP header response, but with Puppet
exec {'confighead':
  provider => shell,
  command  => 'sudo apt-get update && sudo apt-get install -y nginx && echo "Holberton School for the win!" | sudo tee /var/www/html/index.html && sudo chmod -R 777 /etc/nginx && sudo sed -i "/server_name _;/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default && sed -i "11 a \ \tadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf && sudo service nginx restart',
}
