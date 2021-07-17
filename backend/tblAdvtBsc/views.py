from django.shortcuts import render
from rest_framework import generics

from .models import tblAdvtBsc
from .serializers import tblAdvtBscSerializer

class ListtblAdvtBsc(generics.ListCreateAPIView):
    queryset = tblAdvtBsc.objects.all()
    serializer_class = tblAdvtBscSerializer

class DetailtblAdvtBsc(generics.RetrieveUpdateDestroyAPIView):
    queryset = tblAdvtBsc.objects.all()
    serializer_class = tblAdvtBscSerializer