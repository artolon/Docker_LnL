#version of python we are using (the parent image)
FROM python:3 
# working directory within our container
WORKDIR /my_app
# copy all the files from our local directory into docker directory that we just made
COPY . /my_app
# install all the dependencies we need
RUN apt-get update
# command to be executed
CMD ["python3", "breakfast.py"]


