from django.shortcuts import render
from .seralizers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import  IsAdminUser
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class UserViewSet(viewsets.ModelViewSet):
    permission_class = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        # queryset = DatosPrivadosdelProceso.objects.filter(Q(created_by=self.request.user) | Q(subaccount__contains = [self.request.user.id])).order_by('-id')
        print (self.request.user.is_superuser)
        if self.request.user.is_superuser:

            queryset = User.objects.all()
            return queryset 
        return []

class CustomAuthToken(ObtainAuthToken): 
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'id': user.id,
            'token': token.key,
            'email': user.email,
            'username': user.username,
            'subaccount': "true",
            'is_superuser': user.is_superuser,
            })

  