# script to setup containers and create network
# usage: bash container-setup.sh

# create network
docker network create ss-network

# create database
echo "Creating database..."
bash database-setup.sh

# create server
echo "Creating server..."
cd ./server
echo "Building image..."
docker build -t server-image .
bash server-setup.sh
cd ../

# temporary pause because container linking is not instant
echo "Time delay for container linking..."
sleep 10

# create database table
docker exec -it postgres-db bash -c "cd db && psql --username=postgres -w --file=table-create.sql"

# start app server
# docker exec -d server python App/src/app.py

# test all running containers
# sleep 1

# curl localhost:5000/test_server
