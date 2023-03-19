# Docker: Basic vocabulary
*Note: this list is not exhaustive and only covers concepts mentioned during lunch-n-learn*

**Docker Desktop**
-	Graphical user interface (GUI) for Docker

**Docker client**
-	Command line interface for typing and viewing various Docker commands
-	Allows you to view output produced by Docker daemon 

**Docker host**
-	Physical or virtual server on which the core component of Docker operates
-	Provides complete environment to execute and run applications; includes the Docker daemon, images, containers, networks, and storage

**Docker daemon (or dockerd)**
-	Manages docker images and containers
-	Listens for commands and executes them

**Docker registry** 
-	Central location to store all your custom images and share with the world! 

**Docker hub**
-	Docker’s official cloud-based registry
-	Can also search for all the Docker official images 

**Images**
-	A “snapshot” of all the source code, environment variables, and other dependencies required to run your application and/or process
-	Basically a blueprint for your container

**Tag**
-	The “version” of your image
-	Usually formatted as image_name:tag (e.g. python:3)
-	Python is the image name and 3 is the tag

**Repository** 
-	Another way to say image name
-	Allows for versioning 
-	Ex: If I have an image called “breakfast,” then “breakfast” is also the name of the image repository. If I add a tag and push all the versions to a registry, then they will be stored under the same name/repository, but with different version/tag numbers

**Containers**
-	The running unit of software
-	Isolated environment for your image
-	Contains file system, image, and configurations

**Dockerfile**
-	The “instructions” which detail how to build your custom image
-	This file is required to build an image
-	This file has no extension 

**.dockerignore**
-	Like a .gitignore
-	Allows you to write a list of all the files and/or file extensions that you do not want stored within your container
