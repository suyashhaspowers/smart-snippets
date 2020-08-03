# script to start server docker container
# usage: bash server-setup.sh

docker run -d -it --name=server -p 5000:5000 -v $PWD:/App --net=ss-network --env-file variables.env server-image