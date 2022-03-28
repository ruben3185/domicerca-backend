from django.shortcuts import render
from .models import Domicilio
from .serializers import DomiciloSerializers
from rest_framework import viewsets


class DomicilioViewset(viewsets.ModelViewSet):
    queryset = Domicilio.objects.all().order_by('-id')
    serializer_class = DomiciloSerializers


