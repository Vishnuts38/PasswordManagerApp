from django.contrib.auth.models import User
from .models import PasswordItem,PasswordShare,Organisation
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class PasswordSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField()
    class Meta:
        model = PasswordItem  
        fields = ["id","user","user_id","password",]
        depth = 1

    def create(self,validated_data):

        user_id = validated_data.pop('user_id')
        user_obj = User.objects.get(id=user_id)
        password_item = PasswordItem.objects.create(user=user_obj, **validated_data)
        return password_item

class PasswordShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordShare
        fields = '__all__'

class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = '__all__'