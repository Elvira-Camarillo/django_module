# from django.shortcuts import render

from rest_framework import generics

from vet.models import PetOwner, Pet, PetDate, Office

from .serializers import (
    OwnersListSerializer, 
    OwnersSerializer, 
    PetsListSerializer, 
    PetsSerializer, 
    OwnersPetsSerializer,
    PetOwnerSerializer,
    DatesListSerializer,
    DatesSerializer,
    DatesPetSerializer,
    OfficesListSerializer,
    OfficesSerializer
)
# Views Owners
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

# Owner and pets
class RetrieveOwnerPetsAPIView(generics.RetrieveAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersPetsSerializer

## Pets 
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

## Pets and Owners
class RetrievePetsOwnerAPIView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetOwnerSerializer


# Detalle de la mascota más su lista de citas
class ListDatesAPIView(generics.ListAPIView):
    queryset = PetDate.objects.all().order_by("created_at")
    serializer_class = DatesListSerializer

class CreateDatesAPIView(generics.CreateAPIView):
    queryset = PetDate.objects.all()
    serializer_class = DatesSerializer

class RetrieveDatesAPIView(generics.RetrieveAPIView):
    queryset = PetDate.objects.all()
    serializer_class = DatesSerializer

class UpdateDatesListAPIView(generics.UpdateAPIView):
    queryset = PetDate.objects.all()
    serializer_class = DatesSerializer

class DestroyDatesListAPIView(generics.DestroyAPIView):
    queryset = PetDate.objects.all()
    serializer_class = DatesSerializer

# Lista de pets con 
class RetrieveDatesPetAPIView(generics.RetrieveAPIView):
    queryset = PetDate.objects.all()
    serializer_class = DatesPetSerializer

## Lista de oficionas
class ListOfficesAPIView(generics.ListAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficesListSerializer

class CreateOfficesAPIView(generics.CreateAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficesSerializer

class RetrieveOfficesAPIView(generics.RetrieveAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficesSerializer