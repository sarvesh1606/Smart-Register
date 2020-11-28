from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer
from main.models import Signup
# Create your views here.

# REST APIs


@api_view(['GET'])
def apiOverview(request):

    api_urls= {
        'User List': '/userlist/' ,
        'Specific User View': '/userspecific/<user id>/',
        'Create User':'/usercreate/',
        'Update User':'/userupdate/<user id>/',
        'Delete User':'/userdelete/<user id>/',
    
    
    }

#    return JsonResponse("API base point" , safe=False)
    return Response(api_urls)

@api_view(['GET'])
def userList(request):
    
    users= Signup.objects.all()
    serializer= UserSerializer(users , many= True)
    return Response(serializer.data)

@api_view(['GET'])
def userSpecific(request , sk):
    
    users= Signup.objects.get(id=sk)
    serializer= UserSerializer(users , many= False)
    return Response(serializer.data)

@api_view(['POST'])
def userCreate(request):
    
    serializer= UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['POST'])
def userUpdate(request , sk):
    
    users= Signup.objects.get(id=sk)
    serializer= UserSerializer( instance=users , data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def userDelete(request , sk):
    
    user= Signup.objects.get(id=sk)
    user.delete()

    return Response("Task deletion successful")