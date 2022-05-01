from django.shortcuts import render
from requests import ReadTimeout
from docker_data import views as dd_views
import json
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http.response import JsonResponse
# Create your views here.

@api_view(['GET'])
def images(request):
    Images=dd_views.list_images()    
    return JsonResponse(Images, status=status.HTTP_200_OK,safe=False) 

@api_view(['GET'])
def containers(request):
    Containers=dd_views.list_containers()    
    return JsonResponse(Containers, status=status.HTTP_200_OK,safe=False) 
    
