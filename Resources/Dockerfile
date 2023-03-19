# This is a Docker file template and explanation 

# enter the image name from your system or dockerhub
# this is also known as "base" image
FROM node

# set working directory
# this is the working directory in your container (not local)
# we will run all our commands in here
WORKDIR /app

# tell docker which files from our local machine should go into the image
# each dot is one path
# the first dot represents the files outside of the image/container
# with just the first dot, we would be saying, "ALL the folders and files surrounding the image should be copied into the container"
# the second path is the folder INSIDE the image, where those files should be stored
# every image has it's OWN file system (detached from your local)
# if we leave the second path as a dot, then the files will just be saved to the root folder
# if we call it something, it will be saved to a folder within the container
# we will create the folder if it is not created already
# If we set the working directory to /app (as above), then we actually can do the COPY . . because the second . will reference our working directory
COPY . .

# after copying all the files into the image, we want to run a command inside the image
# we would need to run npm install locally to get all the dependencies, so we do the same thing here
# By default, the commands will all run within the root directory of your container
# therefore, we HAVE to set a working directory, so that Docker knows where to actually run all these commands
RUN npm install

# this is where we can store our environmental variables
# you do not need this for every docker file; only if you're app requires it
# can also reference a .env file here instead of hard-coding; doing so would be more secure
ENV key=value

# expose port 80, such that we are listening to port 80 from our local machine
# however, within the docker file, this is mostly for documentation purposes only
# we need to actually specify the port within the command line with -p
# -p 3000:80 means we are listening to port 3000 on the local host, but exposing port 80 within the Docker container
EXPOSE 80

# Remember, these are all instructions to create the image, which is a template!!
# all of these above commands are executed whenever the image is being built; they are instructions for the image
# we only want to START a server if we start a container based on that image; we dont' want to start the server just when we build the image

# CMD is the default command when the container starts up
# the difference between run and cmd is that run will execute when the image is being created and cmd will be executed when the container is being created
# so now, whenever a container is run based on this image, we will execute the "node" command on a "server.js" file
# the commands need to be in an array in string format
# must use double quotes
CMD ["node", "server.js"]

# each container has its own internal network

# CMD is always the LAST command
