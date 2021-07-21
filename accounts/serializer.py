from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.core import exceptions
from django.contrib.auth import password_validation as validators
from django.contrib.auth.hashers import make_password

from .models import UserProfile

User = get_user_model()

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('U', 'Unspecified')
)


class UserProfileSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    full_name = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=15)
    username = serializers.CharField(max_length=255)
    age = serializers.IntegerField(min_value=12)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES)

    # class Meta:
    #     model = UserProfile
    #     fields = ('first_name', 'last_name', 'phone_number', 'username', 'age', 'gender')


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
        UserProfile.objects.create(user=user, age=0)
        return user


class UserSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        profile = instance.profile
        profile.full_name = validated_data.get('full_name')
        profile.phone_number = validated_data.get('phone_number')
        profile.username = validated_data.get('username')
        profile.age = validated_data.get('age')
        profile.gender = validated_data.get('gender')
        profile.save()
        return instance

    def create(self, validated_data):
        pass

    id = serializers.UUIDField(read_only=True)
    email = serializers.EmailField(read_only=True)
    full_name = serializers.CharField(max_length=255, write_only=True)
    phone_number = serializers.CharField(max_length=15, write_only=True)
    username = serializers.CharField(max_length=255, write_only=True)
    age = serializers.IntegerField(min_value=12, write_only=True)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES, write_only=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        profile = UserProfileSerializer(instance.profile).data
        data['full_name'] = profile['full_name']
        data['phone_number'] = profile['phone_number']
        data['username'] = profile['username']
        data['age'] = profile['age']
        data['gender'] = profile['gender']
        return data


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


class ChangePasswordSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    password = serializers.CharField()
    new_password = serializers.CharField()

    @staticmethod
    def validate_new_password(value):
        errors = dict()
        try:
            validators.validate_password(password=value)
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)
        if errors:
            raise serializers.ValidationError(errors)
        return value
