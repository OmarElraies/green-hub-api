from rest_framework import serializers
from .models import Plants, Category, SubCategory, Places
from django.contrib.auth.models import User


class PlantsSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Plants
        fields = '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = SubCategory
        fields = '__all__'

class PlacesSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Places
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    plants = serializers.HyperlinkedRelatedField(many=True, view_name='plants-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'plants')


