# ACCG3

# To setup server:
1. install rabbitmq, celery, flask, numpy
2. setup rabbitmq server
2. get the murtazo.tgz and extract cloudnaca
3. put the nserver.py script from this repo into the cloudnaca folder
4. start flask server with python3.5 nserver.py

# To start workers:
1. install docker
2. pull and run the image from kristofersundequist/acc3
3. config the nserver.py in the navierstokes folder to match with the rabbitmq server
4. start the celery worker with the nserver script
