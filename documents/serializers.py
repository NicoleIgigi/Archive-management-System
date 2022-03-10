from rest_framework import serializers
from .models import Categories, Doc

class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = {
            'id',
            'title',
        }
        model = Categories

class DocSerializer(serializers.ModelSerializer):

    class Meta:
        fields = {
            'id',
            'title'
            'cover',
            'name',
            'description',
            'private',
            'date_created',
        }

        model = Doc

