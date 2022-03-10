from urllib import response
from django.shortcuts import render
from .models import Categories, Doc
from rest_framework import generics
from .serializers import CategoriesSerializer, DocSerializer

# Create your views here.


class ListCategories(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class DetailCategories(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class ListDoc(generics.ListCreateAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer

class DetailDoc(generics.RetrieveDestroyAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer
