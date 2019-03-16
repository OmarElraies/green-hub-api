from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    plants = serializers.HyperlinkedRelatedField(many=True, view_name='plants-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'plants')
