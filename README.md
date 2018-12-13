# UPSS
scrapes and organizes class scheduling information from the PAUL/UniPB platform in order to present the user with an easy way to schedule classes for this University



#Install docker and docker-compose
#first install docker-compose
# download the latest version of Docker Compose:
sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose


#Once installed, enable and start the docker systemd service from a superuser account.

$ sudo systemctl enable docker
$ sudo systemctl start docker


