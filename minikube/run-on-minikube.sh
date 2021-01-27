#!/bin/bash

minikube start --driver virtualbox --bootstrapper=kubeadm

#################################################################################################
# see the list of add-ons
minikube addons list

#################################################################################################
# enable addons
# minikube addons <action> ADDON_NAME

minikube addons enable dashboard
minikube addons enable metrics-server
minikube addons enable ingress

#################################################################################################
# install ambassador ingress addon
# reference: https://minikube.sigs.k8s.io/docs/tutorials/ambassador_ingress_controller/
minikube addons enable ambassador

##################################################################################################
# to work with the Docker daemon on your Mac/Linux host, use the docker-env command in your shell:
# reference:
# https://stackoverflow.com/questions/52310599/what-does-minikube-docker-env-mean#:~:text=The%20command%20minikube%20docker%2Denv,and%20put%20them%20into%20effect.&text=Build%20the%20Docker%20image%20on%20the%20host%20machine.
# This is a workflow optimization intended to improve your experience with building and running Docker images which you can run inside the minikube environment. It is not mandatory that you re-use minikube's Docker daemon to use minikube effectively, but doing so will significantly improve the speed of your code-build-test cycle.

# In a normal workflow, you would have a separate Docker registry on your host machine to that in minikube, which necessitates the following process to build and run a Docker image inside minikube:

# 1. Build the Docker image on the host machine.
# 2. Re-tag the built image in your local machine's image registry with a remote registry or that of the minikube instance.
# 3. Push the image to the remote registry or minikube.
# 4. (If using a remote registry) Configure minikube with the appropriate permissions to pull images from the registry.
# 5. Set up your deployment in minikube to use the image.
#
# By re-using the Docker registry inside Minikube, this becomes:

# 1. Build the Docker image using Minikube's Docker instance. This pushes the image to Minikube's Docker registry.
# 2. Set up your deployment in minikube to use the image

eval $(minikube docker-env)

# this should show all containers running inside minikube
docker ps

# ###############################################################################################
# verify
minikube dashboard

# get the ip address of the minikube
minikube ip

# Verify that the NGINX Ingress controller is running
kubectl get pods -n kube-system

# ###############################################################################################
# deploy to minikube - short version

# cleanup deplyment
kubectl delete deployment guardian-grrf

# deploy
kubectl get namespaces
kubectl create deployment guardian-grrf --image=guardiandev/grrf:latest
kubectl apply -f minikube/minikube-grrf-deployment.yaml

# verify
kubectl get deployments
kubectl get pods
kubectl get events
kubectl config view

# create a service of LoadBalancer
kubectl expose deployment guardian-grrf --type=LoadBalancer --port=8888

# create a service of type NodePort
# this will work with nginx ingress controller
# reference:
# https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/
kubectl expose deployment guardian-grrf --type=NodePort --port=8888

# create a service of ClusterIP
kubectl expose deployment guardian-grrf --type=ClusterIP --port=8888
kubectl apply -f minikube/minikube-grrf-service-clusterip.yaml
kubectl delete -n default service guardian-grrf

# verify
kubectl get services

# this will launch the app using nodeport service address
minikube service guardian-grrf

# ###########################################################
# cleanup everything
kubectl delete service guardian-grrf
kubectl delete deployment guardian-grrf

# ###########################################################
# create ingress resource
# reference: https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/

kubectl apply -f minikube/minikube-grrf-ingress.yaml
kubectl delete -f minikube/minikube-grrf-ingress.yaml


kubectl get ingress

# http://a7672b6438e4145eaa2d248910da463c-809992092.us-east-1.elb.amazonaws.com:8888/





