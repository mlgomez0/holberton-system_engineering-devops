#creating a custom HTTP header response, but with Puppet
exec {'confighead':
  provider => 'shell',
  command  => 'sudo apt-get update && sudo apt-get install -y nginx &&  echo "Holberton School for the win!" | sudo tee /var/www/html/index.html && sudo chmod -R 777 /etc/nginx && sudo sed -i "/server_name _;/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default && sudo touch /usr/share/nginx/html/custom_404.html && echo "Ceci n'est pas une page\n" | sudo tee /usr/share/nginx/html/custom_404.html && sed -i "35 a \ \terror_page 404 /custom_404.html;\n\tlocation = /custom_404.html {\n\t\troot /usr/share/nginx/html;\n\t\tinternal;\n\t}" /etc/nginx/sites-enabled/default &&  sed -i "11 a \ \tadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf && sudo service nginx restart',
}
