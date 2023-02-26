# This is the parent or base image that we are pulling 
FROM python:3.8-slim-buster
# This is the name of the directory for our container (where all these files will go)
WORKDIR /app
# first copy the requirements.txt file into a docker requirements.txt file
COPY requirements.txt requirements.txt
# pip install all our requirements in the container
RUN pip3 install -r requirements.txt
# copy everything else into our /app folder
COPY . .
# set our environment variables, specific for flask app
ENV FLASK_APP=app.py
# this is for documentation purposes. expose container port 5000
EXPOSE 5000
# the commands we need to run for our flask app to work
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]