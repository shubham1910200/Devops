# Docker General Commands

Display Docker version:
```bash 
docker --version
```

Display Docker info:
```bash
    docker info
```

Show system-wide information:
``` bash 
docker system info
```

# Docker Container Commands
List all containers (running and stopped):
``` bash 
docker ps -a
```

List only running containers:
``` bash 
docker ps

Start a container:
```bash 
docker start <container_id_or_name>
```

Stop a container:
``` bash 
docker stop <container_id_or_name>
```

Restart a container:
``` bash 
docker restart <container_id_or_name>
```

Pause a container:
``` bash 
docker pause <container_id_or_name>
```

Unpause a container:
``` bash 
docker unpause <container_id_or_name>
```

Remove a container:
``` bash 
docker rm <container_id_or_name>
```

Remove all stopped containers:
``` bash 
docker container prune
```

Inspect a container:
``` bash 
docker inspect <container_id_or_name>
```

View logs of a container:
``` bash 
docker logs <container_id_or_name>
```

Execute a command in a running container:
``` bash 
docker exec -it <container_id_or_name> <command>
```

# Docker Image Commands

List all images:
```bash 
docker images
```

Pull an image from a registry:
``` bash 
docker pull <image_name>:<tag>
```

Build an image from a Dockerfile:
``` bash 
docker build -t <image_name>:<tag> .
```

Tag an image:
``` bash 
docker tag <image_id> <new_image_name>:<tag>
```

Remove an image:
``` bash 
docker rmi <image_id_or_name>
```
Remove all unused images:
``` bash 
docker image prune
```
Inspect an image:
``` bash 
docker inspect <image_id_or_name>
```
# Docker Volume Commands

List all volumes:
``` bash 
docker volume ls

Create a volume:
``` bash docker volume create <volume_name>
```
Remove a volume:
``` bash
 docker volume rm <volume_name>
```
Inspect a volume:
``` bash
 docker volume inspect <volume_name>
```
Remove all unused volumes:
``` bash
 docker volume prune
```
# Docker Network Commands
List all networks:
``` bash 
docker network ls
```

Create a network:
``` bash
 docker network create <network_name>
```
Remove a network:
``` bash 
docker network rm <network_name>
```
Inspect a network:
``` bash 
docker network inspect <network_name>
```
Remove all unused networks:
``` bash
 docker network prune
```
# Docker System Commands
Show system-wide information:
``` bash
 docker system info
```
Remove unused data (containers, networks, images, volumes):
``` bash
 docker system prune
```
Remove unused data with more aggressive pruning:
``` bash
 docker system prune -a
```
# Docker Compose Commands

Check Docker Compose version:
``` bash
 docker-compose --version
```
Start services defined in docker-compose.yml:
``` bash
 docker-compose up

```
Start services in detached mode:
``` bash
 docker-compose up -d
```
Stop and remove containers, networks, volumes, and images:
``` bash
 docker-compose down
```
Rebuild services:
``` bash 
docker-compose build
```
View logs of services:
``` bash
 docker-compose logs
```
Execute a command in a running service:
``` bash 
docker-compose exec <service_name> <command>
```
Run a one-off command:
``` bash
 docker-compose run <service_name> <command>
```
Remove stopped service containers:
``` bash
 docker-compose down --volumes
```
# Docker Registry Commands

Login to Docker Hub:
```bash
 docker login
```

Logout from Docker Hub:
``` bash 
docker logout
```

Push an image to a registry:
```bash 
docker push <image_name>:<tag>
```