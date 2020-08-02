# stop all containers
# usage: bash stop.sh

# stop database
docker stop postgres-db
docker rm postgres-db

# stop server
docker stop server
docker rm server

# remove network
docker network rm ss-network