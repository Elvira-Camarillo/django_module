from rest_framework import serializers

from vet.models import PetOwner, Pet, PetDate

class OwnersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = [
            "id",
            "first_name",
            "last_name",
        ]


class OwnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = "__all__"



### Adelanto de clase
class PetsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = [
            "id",
            "name"
        ]

class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = "__all__"


class OwnersPetsSerializar(serializers.ModelSerializer):
    pets = PetsListSerializer(many=True)
    
    class Meta:
        model = PetOwner
        fields = ["id", "first_name", "last_name","email","phone", "address", "created_at", "pets"]