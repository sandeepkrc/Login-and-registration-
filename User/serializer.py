from rest_framework import serializers

from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth import password_validation
import random
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class AuthenticationSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['id'] = self.user.id
        data['email'] = self.user.email
        data['username'] = self.user.username
        logger.info(f'User login successfully with this Credentials : {data}')
        return data


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')

    def validate_email(self, emails):
        if User.objects.filter(email=emails).exists():
            raise serializers.ValidationError('email already exist.')
        return emails

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'],
                                        first_name=validated_data['first_name'], last_name=validated_data['last_name'])

        return user


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

