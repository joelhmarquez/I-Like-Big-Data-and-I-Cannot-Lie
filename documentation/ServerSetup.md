# Server Setup

Document in order to help set up your servers

+ Initialize server on AWS
+ Add to security group
+ Inbound IP addresses
  * 22,80,443
+ Add users
  * sudo adduser "username"
+ Add their ssh keys
  * sudo -i
  * cd /home/"username"
  * mkdir .ssh
  * cd .ssh
  * touch authorized_keys
  * vim authorized_keys
  1. Paste in the user’s public key
  * cd ../
  * chown -R "user":"user" .ssh
  * Change ownership of files and folders from root to the user’s
+ Add users to sudo
  * sudo adduser "username" sudo
+ Remove password for sudo on user accounts
  * sudo visudo
+ Put this at the end of the file: 
  * "username" ALL=(ALL) NOPASSWD: ALL
