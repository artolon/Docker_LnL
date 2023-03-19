# Hello Beluga!
## Intro to Docker Exercise: 
### Containerize a flask app

**Folder should contain:**
1. Templates
    - Index.html
2. .dockerignore
3. app.py
4. deleteme.txt
5. random.txt
6. requirements.txt

## Create Image/Container and Explore:
1.	Create Docker file
2.	Build the image with a name
    - Docker build -t beluga .
3. Confirm your image is there!
    - Docker images
4.	Inspect the image
    - Docker inspect beluga
5.	Clone image with a different name
    - Docker tag beluga new_beluga
    - confirm both images are there
6.	Create a container. The container should be in “detached” mode (-d). Make the local port 3000 and the container port 5000 (-p 3000:5000). Give this container a name of your choosing (--name). You can select either of your images for this container (should have 2 images from previous step)
    - Docker run -d -p 3000:5000 --name hello_beluga beluga
7.	Check that your container is running. Do you see the container? Is the name what you expected? Do the ports look correct?
    - Docker ps
8.	Confirm everything is working
    - Look at localhost:3000 
    - Do you see a cute picture of a beluga whale?
9.	Explore your running container!
    - Docker exec -it hello_beluga /bin/bash
    - Run a few basic liunx commands to explore (i.e. ls, cd, cat, nano, etc.)
    - *Side note: You will default to the “app” directory that we created in the docker file. Use “cd ..” to view all the files and folders that come with containers by default*
    - Completely optional, but can delete the __pycache__ directory “rm -r __pycache__” if you want. . Also, delete the “deleteme.txt” file (rm deleteme.txt). Notice how, even if you delete from the container, it is still on your local machine! This is because the container is completely separate 😊
    - Exit interactive terminal when done
10.	Stop your container
    - Docker stop hello_beluga
    - *Side note: this will take a couple seconds, so just be patient*
11.	Confirm it has stopped
    - Docker ps
    - Also, refresh the localhost:3000 (you should no longer have the cure picture)
12.	Confirm it still exists, even though it's not running
    - Docker ps -a
13.	Restart the container
    - Docker start hello_beluga
    - Refresh and confirm it’s still on localhost:3000
14.	Remove both of the images you created earlier (i.e. “beluga” and “new_beluga”)
    - Docker rmi beluga new_beluga
15.	This should successfully work for one of the images, but not for the other image. Why??
- Determine the issue and fix it, so that both images are deleted 
- docker stop hello_beluga
- docker rm hello_beluga
- docker rmi new_beluga

Hooray!! You just built an image from scratch and created workable containers!! 
If time, move to Part 2

## Publish/share your Image!
1.	Provide docker credentials in CLI
    - Docker login (follow prompts for user and password)
2.	Build docker image (or rename current image) in this format
    - Username/imagename:tag
    - *Ex: teurbear/beluga:1*
    - docker build -t teurbear/beluga:1 .
3.	Push your image to the docker hub
    - To push the image, you need a repository name, the image name, and a tag
    - Ex: Docker push teurbear/beluga:1
4.	Go to the docker hub and confirm that your repository is there
    - If you want, can add a description and ReadMe etc.
5.	Within the CLI, remove any images and containers associated with this exercise (if you haven’t already)
6.	Then, pull the image you just pushed to the Docker Hub
    - Ex: Docker pull teurbear/beluga:1
7.	Use docker images to ensure it’s there
8.	Try to create a container and confirm everything is working on your local host!
