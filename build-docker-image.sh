#!/bin/sh

# no entrypoint
# user regularuser
docker build -t guardian/grrf:001 -f docker/Dockerfile .

# ENTRYPOINT ./bootstrap.sh
# user regularuser
docker build -t guardian/grrf:002 -f docker/Dockerfile .


