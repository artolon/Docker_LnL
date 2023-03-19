# What’s for Breakfast?
## Intro to Docker Exercise: 
### Containerize a simple python script

**Folder should contain:**
1. Breakfast.py
2. .dockerignore
3. random.txt (to explain .dockerignore)

### Activity Instructions

### Build an Image:
1.	Create Docker file
2.	Build an image
    - Docker build .
    - The initial build will take a bit of time
3.	Make sure your image is there
    - Docker images
4.	Notice it does not have a name ☹
5.	Name the image
    - Docker tag (imageID) breakfast
    - Note: you should actually name in the build step
    - E.g. Docker build -t breakfast .
6.	Try to containerize this image with “docker run breakfast”; what happens? 
    - Oh no! I’m getting errors! Why is this?
    - *Hint: with docker run, we default to being in “attached” mode. What could that mean?*
    - We’re “attached” in the sense that we can view the output of the container. However, we are not actually able to enter anything
    - We will need to run this container in interactive mode!
7.	Containerize the image in interactive mode this time, so that it works
    - Docker run -it breakfast
8.	Notice that the container is no longer running. Use docker ps -a to view the container name
9.	Try to restart that container. What happens now?
    - By default, “docker start” will run in “detached” mode, so we run into this same issue where we can’t input our values, despite there not being an actual error
10.	Now, try to restart the container in attached and interactive mode, so that we can work with the container again
    - E.g. docker start -a -i f8afc88b9ed4
    - *Note: We need to specify -a for “attached.” We also need to re-emphasize that we’re using the container in interactive mode “-i.” However, we do not need the -t flag because that flag persists from the original “docker run” command that we typed earlier in the exercise

Hooray!! You just built an image from scratch and created workable containers!! 
If time, move to Part 2

### Troubleshooting
1.	Run “docker logs containername” on any container to see logs 
    - This can be good for going back and seeing what actually happened with your containers


