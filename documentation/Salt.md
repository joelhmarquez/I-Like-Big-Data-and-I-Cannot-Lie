# Salt

Helpful references for using salt. Providing ability to access backend remotely

This was created by Micheal Swisher for assistance of other students. 

DISCLAIMER: THIS IS TO HELP LAUNCH YOUR SERVER TO GET ALL OF THE SERVICES SETUP ON THE SERVER. By letting me connect to your server, you still claim full liability for anything that happens. I may be your admin, but not my fault if something catches on fire.

## Pre-requisite
Determine if you need Apache Storm, Cassandra, or Apache web server [I can deploy kafka for you as well, but I don’t know anything about it since the kafka deployment is scripted out for me]. If you don’t need any of these, I can’t really help you but I’m totally cool with you connecting to my system so I can give you basic administration such as updates and generic firewall rules :)

## Setting up system
On AWS console, deploy your server as an EC2 instance and make sure the Operating System is set to Ubuntu
When you get to the security group page, pick from one of the SirDataAlot groups based what your service is. If you’re setting up a cassandra box, do cassandra. For those of you who like to live life on the edge or are installing multiple services, select the “yolo” security group :)

+ SSH into your new server using ssh ubuntu@"your new server ip" -i "your login file you chose to use"
+ Escalate your privileges to administrator sudo -i
+ Run apt-get install salt-minion
+ Get the configuration file to connect to automation server using 
+ wget http://swishertest.site/static/minion
+ Update your server config file cat minion > /etc/salt/minion
+ Refresh the service so I can connect to it service salt-minion restart
+ Shoot swish an email at michael.v.swisher@colorado.edu
+ Include what the external IP and the private dns, and what service you want running on it. 

If you want to get fancy and would like to add your own ssh key to the ubuntu account, send me a copy of your public sshkey as well. That’s it! I’ll take care of the rest because I’m awesome. Nuff said. 

## Resources
+ https://docs.saltstack.com/en/latest/topics/development/conventions/formulas.html#adding-a-formula-directory-manually
+ https://docs.saltstack.com/en/latest/topics/tutorials/walkthrough.html#using-salt-key
+ https://repo.saltstack.com/#ubuntu
+ https://docs.saltstack.com/en/latest/ref/configuration/index.html
+ https://docs.saltstack.com/en/latest/topics/execution/remote_execution.html
