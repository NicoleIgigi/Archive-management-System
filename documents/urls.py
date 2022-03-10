from django.urls import path, include
from django.contrib import admin
from . import views
import documents
from .views import DetailCategories, ListCategories, ListDoc, DetailDoc

urlpatterns = [
     path('Categories/', ListCategories.as_view(), name = 'category'),
     path('Categories/<int:pk>/', DetailCategories.as_view(), name ='singlecategory'),    
     path('Doc/', ListDoc.as_view(), name = 'document'),
     path('Doc/<int:pk>/', DetailDoc.as_view(), name ='singledocument'),
]