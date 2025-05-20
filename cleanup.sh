# cleanup.sh
#!/bin/bash
docker-compose down
docker images -f "dangling=true" -q | sort -u | xargs -r docker rmi
docker container prune -f
docker volume prune -f
docker builder prune -f
