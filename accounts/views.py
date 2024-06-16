#from django.shortcuts import render

# Create your views here.

# accounts/views.py
from rest_framework import viewsets
from .models import Account
from .serializers import AccountSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

