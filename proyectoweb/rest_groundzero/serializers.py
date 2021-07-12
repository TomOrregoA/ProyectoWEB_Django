from rest_framework import serializers
from app.models import Obra

class ObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obra
        fields = ['idObra', 'title', 'price', 'heigth', 'width', 'year', 'image', 'style', 'autor']
