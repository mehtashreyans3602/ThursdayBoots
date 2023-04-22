from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ShoeSerializer
from .models import Shoe
from rest_framework import generics
from faker import Faker
import random

class ShoeList(generics.ListCreateAPIView):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer

class ShoeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer

def index(req):
    return render(req,'index.html')

def dummy_data(request):
    fake = Faker()

    # List of possible values for gender
    genders = ['Men', 'Women', 'Unisex']

    # List of possible values for material
    materials = ['Leather', 'Synthetic', 'Canvas', 'Mesh']

    # List of possible values for style
    styles = ['Running', 'Casual', 'Formal', 'Sports', 'Sneakers']

    # List of possible colors
    colors = ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Orange', 'Black', 'White']

    # Generate 50 dummy Shoe objects
    for i in range(50):
        shoe = Shoe(
            model_name=fake.word(),
            color=random.choice(colors),
            size=random.randint(6, 13),
            price=random.randint(50, 200),
            material=random.choice(materials),
            style=random.choice(styles),
            description=fake.text(),
            photo="https://unsplash.com/photos/qxcQG21m_qE",
            gender=random.choice(genders),
        )
        shoe.save()
    message = 'Dummy data created successfully.'
    return render(request,'dummydata.html', {'message': message})