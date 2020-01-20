from django.contrib.auth.models import User
from rest_framework import serializers

from quickstart.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'first_name', 'last_name', 'password']
