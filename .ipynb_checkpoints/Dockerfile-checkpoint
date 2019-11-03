FROM python:3.6-slim


MAINTAINER Stephen Carmody "stephen.m.carmody@gmail.com"


RUN apt -y update &&\
    apt -y install python3 python3-pip

RUN python3 -m pip install --upgrade pip
 
ADD ./python_requirements.txt /
RUN python3 -m pip install -r python_requirements.txt

WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["python3","ml_api.py"]


