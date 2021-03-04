from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.core import exceptions
from django.contrib.auth import password_validation as validators
from django.contrib.auth.hashers import make_password

from .models import UserProfile

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'phone_number', 'username', 'age', 'gender')


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}, }

    def validate(self, data):

        # here data has all the fields which have validated values
        # so we can create a User instance out of it
        user = User(**data)

        # get the password from the data
        password = data.get('password')

        errors = dict()
        try:
            # validate the password and catch the exception
            validators.validate_password(password=password, user=user)

        # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super(CreateUserSerializer, self).validate(data)

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            password=make_password(validated_data['password'], salt=None, hasher='default')
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')


class LoginSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'}, trim_whitespace=False
    )

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            if User.objects.filter(email=email).exists():
                user = authenticate(request=self.context.get('request'), email=email, password=password)
            else:
                msg = {'detail': 'Email not found', 'status': False}
                raise serializers.ValidationError(msg)
            if not user:
                msg = {'detail': 'Email and password are not matching, Try again', 'status': False}
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = {'detail': 'Email address and password not found in request', 'status': False}
            raise serializers.ValidationError(msg, code='authorization')
        data['user'] = user
        return data


class RefreshTokenSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    refresh_token = serializers.CharField()
