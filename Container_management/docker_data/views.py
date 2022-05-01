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
        data.append(("id: "+ container.id,\
                     "name: " + str(container.name),\
                    "Image: "+ str(container.attrs['Config']['Image']),\
                    "Status: "+container.status,\
                    "Environment: "+  str(container.attrs['Config']['Env']),\
                    "Entrypoint: "+ str(container.attrs['Config']['Entrypoint']),\
                    "Volumes: "+ str(container.attrs['Config']['Volumes']),\
                   # "Network: "+str(container.attrs['Config']['Network']),\
                    "Ports: "+ str(container.ports)
                    ))

    return data

def logs_container(id):
    client = docker.from_env()
    container = client.containers.get(id)
    logs={"log": container.logs().decode('utf-8')}
    return logs


def run_container(Image,command,ports):
    
    return 0