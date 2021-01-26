#!/bin/sh

docker run -it  \
    --name guardian-grrf \
    -p 8888:8888 \
    -p 8000:8000 \
    --rm \
    guardian/grrf:001 bash

docker run -it  \
    --name guardian-grrf \
    -p 8888:8888 \
    --rm \
    guardian/grrf:001 /mainsite/bootstrap.sh

##########################################################################################

docker run -itd  \
    --name guardian-grrf \
    -p 8888:8888 \
    --rm \
    guardian/grrf:002


docker exec -it guardian-grrf ls ./


python manage.py runserver 8888

