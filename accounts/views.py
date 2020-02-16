from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings
from .serializer import CreateUserSerializer
from rest_framework.permissions import AllowAny
import requests
# from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

CLIENT_ID = settings.CLIENT_ID
CLIENT_SECRET = settings.CLIENT_SECRET


# Create your views here.
class Register(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', False)
        password = request.data.get('password', False)
        print(request.data.get('email'), "request data")
        if email and password:
            temp_data = {
                'email': email,
                'password': password
            }

            serializer = CreateUserSerializer(data=temp_data)
            serializer.is_valid(raise_exception=True)
            if serializer.is_valid():
                user = serializer.save()

                r = requests.post(
                    'http://0.0.0.0:8000/o/token/',
                    data={
                        'grant_type': 'client_credentials',
                        'username': email,
                        'password': password,
                        'client_id': CLIENT_ID,
                        'client_secret': CLIENT_SECRET,
                        'scope': 'read'
                    },
                )
                # If it goes well return sucess message (would be empty otherwise)
                print(r.json())
                if r.status_code == requests.codes.ok:
                    return Response(r.json(), r.status_code)
                # Return the error if it goes badly
                return Response({"details": r.json()}, r.status_code)
            return Response(serializer.errors)

        else:
            return Response({"detail": "Please input e-mail address and password correctly"},
                            status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        '''
        Gets tokens with username and password. Input should be in the format:
        {"username": "username", "password": "1234abcd"}
        '''
        r = requests.post(
            'http://0.0.0.0:8000/o/token/',
            data={
                'grant_type': 'password',
                'email': request.data['email'],
                'password': request.data['password'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )
        return Response(r.json())


class RefreshToken(APIView):

    def post(self, request):
        '''
        Registers user to the server. Input should be in the format:
        {"refresh_token": "<token>"}
        '''
        r = requests.post(
            'http://0.0.0.0:8000/o/token/',
            data={
                'grant_type': 'refresh_token',
                'refresh_token': request.data['refresh_token'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )
        return Response(r.json())


class Logout(APIView):
    def post(self, request):
        '''
        Method to revoke tokens.
        {"token": "<token>"}
        '''
        r = requests.post(
            'http://0.0.0.0:8000/o/revoke_token/',
            data={
                'token': request.data['token'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )
        # If it goes well return sucess message (would be empty otherwise)
        if r.status_code == requests.codes.ok:
            return Response({'message': 'token revoked'}, r.status_code)
        # Return the error if it goes badly
        return Response(r.json(), r.status_code)
