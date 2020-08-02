# script to setup postgres database
# usage: bash database-setup.sh

# run postgres container
docker run -d -it --name=postgres-db -e POSTGRES_PASSWORD=smartsnippet --expose 5432 --net=ss-network -v $PWD:/db postgres