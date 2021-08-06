from rest_framework.serializers import ModelSerializer
from .models import *


class CategorySerializer(ModelSerializer):
    class Meta:
        model = LoaiHinhDuLich
        fields = ['id', 'name']


class TourSerializer(ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Tour
        fields = ['id', 'name', 'image', 'NgayKhoiHanh', 'SoNgay', 'Gia', 'content','category']

