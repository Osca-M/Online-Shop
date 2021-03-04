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

from .serializer import CreateUserSerializer, LoginSerializer, RefreshTokenSerializer

CLIENT_ID = "Application.objects.get(name='commerce').client_id"
CLIENT_SECRET = "Application.objects.get(name='commerce').client_secret"


# Create your views here.
class Register(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def post(request, *args, **kwargs):
        with transaction.atomic():
            email = request.data.get('email', False)
            password = request.data.get('password', False)
            if get_user_model().objects.filter(email=email).exists():
                return Response({'detail': 'User with such a mail address exists'}, status=status.HTTP_400_BAD_REQUEST)
            if email and password:
                temp_data = {'email': email, 'password': password}

                serializer = CreateUserSerializer(data=temp_data)
                serializer.is_valid(raise_exception=True)
                if serializer.is_valid():
                    user = serializer.save()
                    user_client_id = generate_client_id()
                    user_client_secret = generate_client_secret()
                    # try:
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

                    oauth2_application = get_application_model().objects.create(**oauth2_application_data_object)
                    oauth2_application.save()
                    # except json.JSONDecodeError: return Response({"details": "Trouble creating the account"},
                    # status=status.HTTP_400_BAD_REQUEST)

                    # r = requests.post(
                    #     'http://0.0.0.0:8000/o/token/',
                    #     data={
                    #         'grant_type': 'password',
                    #         'username': email,
                    #         'password': password,
                    #         'client_id': oauth2_application.client_id,
                    #         'client_secret': oauth2_application.client_secret
                    #     },
                    # )
                    # # If it goes well return sucess message (would be empty otherwise)
                    # print(r.status_code)
                    # if r.status_code == requests.codes.ok:
                    #     return Response(r.json(), r.status_code)
                    # # Return the error if it goes badly
                    # return Response({"details": r.json()}, r.status_code)
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
        Gets tokens with username and password. Input should be in the format:
        {"username": "username", "password": "1234abcd"}
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
        Registers user to the server. Input should be in the format:
        {"refresh_token": "<token>"}
        """
        serializer = RefreshTokenSerializer(data=request.data)
        if serializer.is_valid():
            try:
                token_details = get_object_or_404(
                    get_refresh_token_model(), token=serializer.validated_data.get('refresh_token')
                )
            except get_refresh_token_model().DoesNotExist:
                return Response({'details': 'Refresh token does not exist'}, status=status.HTTP_404_NOT_FOUND)

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
        Method to revoke tokens.
        {"token": "<token>"}
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
