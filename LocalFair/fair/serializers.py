from rest_framework import serializers
from django.contrib.auth.models import User


from .models import Dich, Dich2, Product


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = User
        fields = ['id', 'username', 'url']


class DichSerialazer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Dich
        fields = '__all__'

class Dich2Serialazer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Dich2
        fields = '__all__'

# 'url' in fields - ссылка на данные допользователя /api/users/1/

class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = '__all__'


