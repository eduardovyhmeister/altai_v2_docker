FROM python:3.10
LABEL maintainer="eduardo vyhmeister - insight centre"

#define that all errors are sent to terminal
ENV PYTHONUNBUFFERED=1

#this is the name of the directory in the container that everything will be set
WORKDIR /taiprm_altai

#set all packeges to run
COPY requirements.txt requirements.txt

#create the environment
RUN python -m venv /py && \
    /py/bin/pip3 install --upgrade pip && \
    /py/bin/pip3 install -r requirements.txt && \
    adduser --disabled-password --no-create-home eduardo
# last line es to create a user and avoid to run from the overal system. SECURITY

ENV PATH="/py/bin:$PATH"

USER eduardo 


#las line is to run as eduardo and not root user

#copy across everythin # this is removed since a link between folders was created
#COPY . .

#thir run whatever you want in the environment #this is removed since is run in the docker-compose file
#CMD ["python3","manage.py","runserver","0.0.0.0:8000"]



