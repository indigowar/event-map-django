from django.contrib.auth.hashers import make_password

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'is_staff', 'is_superuser')


class OnlyIDUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)
        read_only_fields = ('id',)


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name',)
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def validate_password(self, password: str) -> str:
        return make_password(password)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta().model(**validated_data)
        instance.is_active = True
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
