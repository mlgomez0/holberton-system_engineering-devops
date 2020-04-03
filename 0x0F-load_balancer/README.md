#0x0F. Load balancer
This is a Holberton School educational project.

#Concepts explored

- Configurating a HTTP response
- Configurating a load balancer

#Installation

Files will be interpreted on Ubuntu 16.04 LTS


## Usage

Educational purposes

## Tasks (to run the script values has to be passed as arguments)
0. 0-custom_http_response-header: Bash script that configures a new Ubuntu machine(Install nginx on your web-02 server, Nginx should be listening on port 80, When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a HTTP response X-Served-By: 03-web-01.
1. 1-install_load_balancer: Script that configures HAproxy with version equal or greater than 1.5 so that it send traffic to web-01 and web-02
- Distribute requests using a roundrobin algorithm
- Make sure that HAproxy can be managed via an init script
- Make sure that your servers are configured with the right hostnames: [STUDENT_ID]-web-01 and [STUDENT_ID]-web-02. If not, follow this tutorial.
- For your answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements
