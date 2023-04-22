from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ShoeSerializer
from .models import Shoe
from rest_framework import generics
class ShoeList(generics.ListCreateAPIView):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer

class ShoeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer

def index(req):
    return render(req,'index.html')