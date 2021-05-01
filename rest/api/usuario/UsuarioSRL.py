
from rest_framework import serializers
from django.contrib.auth.models import User


class usuarioserializado (serializers.ModelSerializer):
    username = serializers.CharField(required = False)
    email = serializers.EmailField(required= False )

    class Meta :
        model = User 
        fields = ['username','email']
