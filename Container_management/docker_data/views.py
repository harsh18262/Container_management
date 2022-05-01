from django.http import HttpResponse
from django.shortcuts import render
import docker
# Create your views here.

def list_images():
    client = docker.from_env()
    images=client.images.list()
    client.close()
    data=[]
    for image in images:
        data.append(("id: "+ image.id,"name: " + str(image.tags)))

    return data

def list_containers():
    client = docker.from_env()
    containers=client.containers.list(all=True)
    client.close()
    data=[]
    for container in containers:
        if container.image.tags == []:
            Image=str(container.image.id)
        else:
            Image=str(container.image.tags)
        data.append(("id: "+ container.id,\
                     "name: " + str(container.name),\
                    "Image: "+ Image,\
                    "Status: "+container.status,\
                   # "Environment: "+ container.environment,\
                   # "Volumes: "+ str(container.volumes),\
                 #   "Network: "+container.network,\
                    "Ports: "+ str(container.ports)
                    ))

    return data