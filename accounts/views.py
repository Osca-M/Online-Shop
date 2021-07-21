import requests

from django.contrib.auth import get_user_model
from django.db import transaction
from django.shortcuts import get_object_or_404

from oauth2_provider.generators import generate_client_id, generate_client_secret
from oauth2_provider.models import get_application_model, get_refresh_token_model, get_access_token_model

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializer import CreateUserSerializer, LoginSerializer, RefreshTokenSerializer, UserSerializer
User = get_user_model()
CLIENT_ID = "Application.objects.get(name='commerce').client_id"
CLIENT_SECRET = "Application.objects.get(name='commerce').client_secret"


# Create your views here.
class Register(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def post(request, *args, **kwargs):
        """
        Creates a User account with email and password. Request payload should be in the format:
        {"email": "mail@example.com", "password": "1234abcd"}
        """
        with transaction.atomic():
            email = request.data.get('email', False)
            password = request.data.get('password', False)
            if get_user_model().objects.filter(email=email).exists():
                return Response({'detail': 'User with such a mail address exists'}, status=status.HTTP_400_BAD_REQUEST)
            if email and password:
                temp_data = {'email': email, 'password': password}
                serializer = CreateUserSerializer(data=temp_data)
                if serializer.is_valid():
                    user = serializer.save()
                    user_client_id = generate_client_id()
                    user_client_secret = generate_client_secret()

                    oauth2_application_data_object = {
                        'user': user,
                        'client_id': user_client_id,
                        'client_secret': user_client_secret,
                        'name': email,
                        'skip_authorization': True,
                        'redirect_uris': '',
                        'client_type': 'confidential',
                        'authorization_grant_type': 'password'
                    }
                    get_application_model().objects.create(**oauth2_application_data_object)

                    return Response({'detail': 'User created successfully'}, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response(
                    {'detail': 'Please input e-mail address and password correctly'}, status=status.HTTP_400_BAD_REQUEST
                )


class LoginView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def post(request):
        """
        Gets Oauth2 tokens with email and password. request payload structure should be in the format:
        {"email": "mail@example.com", "password": "1234abcd"}
        """
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                application_model = get_application_model().objects.get(name=serializer.validated_data.get('email'))
            except get_application_model().DoesNotExist:
                return Response({'detail': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
            user_client_id = application_model.client_id
            user_client_secret = application_model.client_secret
            scheme = request.is_secure() and 'https' or 'http'
            url = scheme + '://' + request.get_host() + '/o/token/'
            r = requests.post(
                url,
                data={
                    'grant_type': 'password',
                    'username': request.data['email'],
                    'password': request.data['password'],
                    'client_id': user_client_id,
                    'client_secret': user_client_secret,
                    'refresh_token': True,
                    "scope": "read"
                },
            )
            return Response(r.json())

        else:
            return Response({'detail': 'Incorrect email or password'}, status=status.HTTP_400_BAD_REQUEST)


class RefreshToken(APIView):

    @staticmethod
    def post(request):
        """
        Generates new Oauth2 tokens for a logged in user. Request payload structure should be in the
        following structure. The refresh token should be valid:
        {"refresh_token": "<token>"}
        """
        serializer = RefreshTokenSerializer(data=request.data)
        if serializer.is_valid():
            try:
                token_details = get_object_or_404(
                    get_refresh_token_model(), token=serializer.validated_data.get('refresh_token')
                )
            except get_refresh_token_model().DoesNotExist:
                return Response({'detail': 'Refresh token does not exist'}, status=status.HTTP_404_NOT_FOUND)

            user = get_object_or_404(get_application_model(), user_id=token_details.user_id)
            user_client_id = user.client_id
            user_client_secret = user.client_secret
            scheme = request.is_secure() and 'https' or 'http'
            url = scheme + '://' + request.get_host() + '/o/token/'
            r = requests.post(
                url,
                data={
                    'grant_type': 'refresh_token',
                    'refresh_token': serializer.validated_data.get('refresh_token'),
                    'client_id': user_client_id,
                    'client_secret': user_client_secret,
                },
            )
            return Response(r.json())
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    @staticmethod
    def post(request):
        """
        Method to revoke tokens. Requires an authenticated user
        """
        authorization = request.headers.get('Authorization')
        token = authorization.split(' ')[1]
        try:
            token_details = get_object_or_404(get_access_token_model(), token=token)
        except get_access_token_model().DoesNotExist:
            return Response({'detail': 'Token does not exist'}, status=status.HTTP_404_NOT_FOUND)

        user = get_object_or_404(get_application_model(), user_id=token_details.user_id)
        user_client_id = user.client_id
        user_client_secret = user.client_secret
        scheme = request.is_secure() and 'https' or 'http'
        url = scheme + '://' + request.get_host() + '/o/revoke_token/'
        r = requests.post(
            url,
            data={'token': token, 'client_id': user_client_id, 'client_secret': user_client_secret},
        )
        # If it goes well return success message (would be empty otherwise)
        if r.status_code == requests.codes.ok:
            return Response({'detail': 'Logged out successfully'}, r.status_code)
        # Return the error if it goes badly
        return Response(r.json(), r.status_code)


class ProfileView(APIView):
    @staticmethod
    def get(request):
        """
        Gets the user profile a the logged in user
        """
        user = get_object_or_404(User, email=request.user)
        return Response(UserSerializer(user).data)

    @staticmethod
    def put(request):
        """
        Updates the user profile of the logged in user
        """
        user = get_object_or_404(User, email=request.user)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
