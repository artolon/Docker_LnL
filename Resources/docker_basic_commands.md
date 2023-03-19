# Docker: Basic commands
*Note: this list is not exhaustive and only covers concepts mentioned during lunch-n-learn*

## Images

Docker pull
-	Pull an image directly from the Docker hub (ex: docker pull python:3)

Docker build .
-	Build your custom image from a Dockerfile

Docker build -t image_name .
-	Build your custom image from Dockerfile and call it “image_name”

Docker images
-	View a list of all the images you have stored locally

Docker inspect image_name
-	View the contents of your image

Docker tag OLD_NAME NEW_NAME 
-	Clone an image with a different name

Docker rmi image_name
-	Remove an image (delete it)

Docker image prune
-	Remove ALL unused images at the same time

Docker ps
-	Display a list of running containers

Docker ps –a
-	Display a list of all containers, whether running or not

## Containers

Docker run image_name
-	Create a NEW container, based on an image
-	Note: This command is also a shortcut because if you don’t already have the image locally, docker will automatically complete the “pull” command before doing the “run” command
-	With docker run, the “attached” mode is the default, so once you run the command, you won’t be able to type any additional commands in the terminal (while container is actively running)
	- 	Attached means that we are listening to the output of that container
	
Docker run –d
-	Start new container in a detached mode 
	- This way, our terminal is not attached to the running container; this allows us to close the terminal and keep the container running
-	You will get the ID of the container as an output
-	If you are in detached mode, and you want to attach yourself back to the container, you can just type “docker attach container_name”

Docker run -it
-	Run your container in interactive mode; this is good for when you have a container that requires you to interact with the terminal (ex: input commands in python script)

Docker start container_name
-	This is to RESTART a container that was already stopped. Use docker start [insert container ID] to restart the stopped container, and it will retain all of its attributes
-	With Docker start, the default is for it to be in the “detached” mode, so you can continue to type commands afterwards
-	If you want to be in attached mode and be interactive, can add the -a and -i flags (docker start container_name -a -i)

Docker stop container_name
-	Stop a container that is actively running

Docker rm container_name
-	Once container is stopped, remove/delete it
-	When executing the “docker run” command with all of the configurations, you can also add a - -rm flag to automatically remove/delete it, once it is stopped

Docker container prune
-	Remove ALL stopped containers 

Docker exec –it container_name /bin/bash
-	Explore the file system of your running container
-	Execute basic Linux commands

Docker logs container_name
-	Will show you a log of what has been going on with your container. This is very helpful for troubleshooting!

## Docker Hub / Other 

Docker login
-	Login to the docker hub

Docker push
-	Once logged into docker hub, can push images there

Docker --help
-	Can get help with any command!

## Common flags
-a, -d, -p, -e, -it, --name, --rm, --help

## Putting it all together
docker run -p 3000:80 -d --name feedback-app --rm feedback-node 
-	Create a new detached container from image (feedback-node), which is listening on local host 3000 and exposing container port 80. The name of the container is “feedback-app,” and we will automatically remove it, once it is stopped
Docker run -it --name break_container breakfast
-	Create a new container (in attached mode) where we can continue to interact with the terminal. Name the container “break_container,” which is based off an image called “breakfast”

