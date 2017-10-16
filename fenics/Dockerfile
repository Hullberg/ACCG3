
#RUN apt-get update -y
#RUN apt-get install -y python-pip python-dev build-essential

# Flower
#
# VERSION 0.1

FROM ubuntu:trusty


# update the package repository and install python pip
RUN apt-get -y update && apt-get -y install python-dev python-pip

# installing flower
RUN pip install flower

# Make sure we expose port 5555 so that we can connect to it
EXPOSE 5555

# Running flower
ENTRYPOINT ["flower", "--port=5555"]
RUN pip install flask
RUN pip install -r requirements.txt
