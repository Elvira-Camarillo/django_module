# from django.shortcuts import render

from rest_framework import generics

from vet.models import PetOwner, Pet, PetDate

from .serializers import (
    OwnersListSerializer, 
    OwnersSerializer, 
    PetsListSerializer, 
    PetsSerializer, 
    OwnersPetsSerializar
)

class ListOwnersAPIView(generics.ListAPIView):
    queryset = PetOwner.objects.all().order_by("created_at")
    serializer_class = OwnersListSerializer

class CreateOwnersAPIView(generics.CreateAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

class RetrieveOwnersAPIView(generics.RetrieveAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

class UpdateOwnersListAPIView(generics.UpdateAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

class DestroyOwnersListAPIView(generics.DestroyAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

##MAscotas y 
class RetrieveOwnerPetsAPIView(generics.RetrieveAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersPetsSerializar

class ListPetsAPIView(generics.ListAPIView):
    queryset = Pet.objects.all().order_by("created_at")
    serializer_class = PetsListSerializer

class CreatePetsAPIView(generics.CreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer

class RetrievePetsAPIView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer

class UpdatePetsListAPIView(generics.UpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer

class DestroyPetsListAPIView(generics.DestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer
