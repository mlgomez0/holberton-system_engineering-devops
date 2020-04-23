#0x14. Mysql
This is a Holberton School educational project.

#Concepts explored

- What is the main role of a database
- What is a database replica
- What is the purpose of a database replica
- Why database backups need to be stored in different physical locations
- What operation should you regularly perform to make sure that your database backup strategy actually works

## Usage

Educational purposes

## Tasks
0. Install Mysql in both servers web-01 and web-02.
1. Create a MySQL user named holberton_user
2. Create a database named tyrell_corp.
3. On your primary MySQL server (web-01), create a new user for the replica server.
4. 4-mysql_configuration_primary, 4-mysql_configuration_replica: MySQL primary must be hosted on web-01 - do not use the bind-address, just comment out this parameter, MySQL replica must be hosted on web-02.
5. 5-mysql_backup: Bash script that generates a MySQL dump and creates a compressed archive out of it.
