# Daily-Diet-Api
Project of an API to register and control meals of an user. Made in Python with Flask.

# Requirements
- Install Python 
https://www.python.org/ 
- Install Docker
https://www.docker.com/products/docker-desktop/

# Run Docker for MySql

Requires docker desktop installed.\
On bash run **one** of this

```sh
docker-compose up

docker-compose up -d #does not lock the terminal

docker-compose up --force-recreate # if its already running
```

# Installation

Use the following command on the terminal

```sh
pip3 install -r requirements.txt
```
create data bases with flask shell

```sh
# Enters the flask shell on the terminal
flask shell

# Creates database
db.create_all() #create tables
db.session.commit() # commits changes

# create user
user = User(username="admin")
db.session.add(user)
db.session.commit()

exit() #quits flask shell
```

# Api Documentation

https://documenter.getpostman.com/view/2850031/2sA2r8248w


# Libs

- Flask
- Flask SQL Alchemy