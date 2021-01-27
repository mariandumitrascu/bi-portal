#!/bin/sh

# no entrypoint
# user regularuser
docker build -t guardian/grrf:001 -f docker/Dockerfile .

# ENTRYPOINT ./bootstrap.sh
# user regularuser
docker build -t guardian/grrf:002 -f docker/Dockerfile  --no-cache .

# build to be uploaded to docker repository
docker build -t guardian/grrf -f docker/Dockerfile  --no-cache .


###############################################################
# push image to docker

# authenticate
docker login --username=dataquadrant
docker login --username=guardiandev
docker logout

docker tag 5bb24b5bf4a2 guardiandev/grrf:001
docker push guardiandev/grrf:001

# ##############################################################
# ##############################################################
# ##############################################################
# build docker image and push to repo, start to finish
docker build -t guardian/grrf -f docker/Dockerfile  --no-cache .
DIMAGE=guardian/grrf
IMAGEID=$( docker images -q ${DIMAGE}:latest )
echo $IMAGEID

docker tag ${IMAGEID} guardiandev/grrf:latest
docker push guardiandev/grrf:latest
# ##############################################################
# ##############################################################
# ##############################################################


