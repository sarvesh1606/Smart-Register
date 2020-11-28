from rest_framework import serializers
from main.models import Signup

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        #fields = ['id', 'username', 'email']
        fields = '__all__'        