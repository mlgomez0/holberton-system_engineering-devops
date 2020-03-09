#0x09. Web infrastructure design

- Network Basics
- Server, Web Server, Application Server
- DNS
- Load Balancer
- Monitoring
- Databases
- DNS Record Types
- Single Point of Failure
- HTTPS
- Firewall
#Contain

Images with different web architectures


## Usage

Educational purposes

## Tasks
- 0-simple_web_stack = link to the following web infrastructure: 1 server, 1 web server (Nginx), 1 application server, 1 application files (your code base)
1 database (MySQL), 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8.
- 1-distributed_web_infrastructure = link to the following added to previous web infrastructure: 2 servers, 1 web server (Nginx), 1 application server
1 load-balancer (HAproxy), 1 set of application files (your code base), 1 database (MySQL) 
- 2-secured_and_monitored_web_infrastructure = link to the following added to previous web infrastructure: 3 firewalls, 1 SSL certificate to serve www.foobar.com over HTTPS, 3 monitoring clients (data collector for Sumologic or other monitoring services)
