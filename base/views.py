from ast import Return
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .serializers import RegisterSerializer, RegisterSerializers, UserSerializer, UpdateSerializer
from rest_framework import generics
from rest_framework.response import Response

class RegisterArchmaApiView(generics.GenericAPIView):
    serializer_class = RegisterSerializers

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"user":"Thank you!, your registration is successful"})


@api_view(['POST'])
def login_archma_api(request):
    Serializer = AuthTokenSerializer(data=request.data)
    Serializer.is_valid(raise_exception=True)
    user = Serializer.validated_data['user']


    created, token = AuthToken.objects.create(user)

    _, token = AuthToken.objects.create(user)

    return Response({
        'user_info' : {
            'id' : user.id,
            'username' : user.username,
            'email' : user.email
        },
        'token' : token

    })

@api_view(['GET'])
def get_user_data(request):
        user = request.user

        if user.is_authenticated:
            return Response({
                'user_info' : {
                'id' : user.id,
                'username' : user.name,
                'email' : user.email
                },
            })
        return Response({'error': 'not authenticated'}, status = 400)

@api_view(['POST'])
def register_api(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.save()

    _, token = AuthToken.objects.create(user)

    return Response({
        'user_info' : {
            'id' : user.id,
            'username' : user.name,
            'email' : user.email
        },
        'token' : token

    })
            

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def files(request):
    return render(request, 'files.html')


from django.contrib.auth.models import User
from .serializers import UserSerializer, UpdateSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class ArchmaUserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ArchmaUpdateUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateSerializer
    lookup_field = 'pk'