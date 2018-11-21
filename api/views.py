from django.shortcuts import render

# Create your views here.

from rest_framework import generics

from pruebas.models import Prueba
from pruebas.models import Deduccion
from pruebas.models import Inferencia
from .serializers import PruebaSerializer
from .serializers import DeduccionSerializer
from .serializers import InferenciaSerializer

class PruebaAPIView(generics.ListCreateAPIView):
    queryset = Prueba.objects.all()
    serializer_class = PruebaSerializer

class PruebaAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prueba.objects.all()
    serializer_class = PruebaSerializer

class PruebaAPIAllView(generics.ListAPIView):
    queryset = Prueba.objects.all()
    serializer_class = PruebaSerializer

class DeduccionAPIView(generics.ListCreateAPIView):
    queryset = Deduccion.objects.all()
    serializer_class = DeduccionSerializer
    
class DeduccionAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deduccion.objects.all()
    serializer_class = DeduccionSerializer
    
class DeduccionAPIAllView(generics.ListAPIView):
    queryset = Deduccion.objects.all()
    serializer_class = DeduccionSerializer

class InferenciaAPIView(generics.ListCreateAPIView):
    queryset = Inferencia.objects.all()
    serializer_class = InferenciaSerializer
    
class InferenciaAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inferencia.objects.all()
    serializer_class = InferenciaSerializer
    
class InferenciaAPIAllView(generics.ListAPIView):
    queryset = Inferencia.objects.all()
    serializer_class = InferenciaSerializer