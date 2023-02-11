from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


class LoginView(GenericAPIView):
    permission_classes =[]
    def post(self, request, *args, **kwargs):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
        except:
            return Response('please provide both email and password', status.HTTP_400_BAD_REQUEST)
    
        user = authenticate(username=username, password=password)
       
        print(user)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user': user.id
                    
                },
            )
        else:
            return Response('invalid authentication credentials', status=status.HTTP_400_BAD_REQUEST)


    