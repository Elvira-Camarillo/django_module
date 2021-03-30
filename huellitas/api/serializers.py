from rest_framework import serializers

from django.contrib.auth.models import User

from vet.models import PetOwner, Pet, PetDate, Office

# Owners
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

### Pets
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

## Ownner with Pets
class OwnersPetsSerializer(serializers.ModelSerializer):
    pets = PetsListSerializer(many=True)
    
    class Meta:
        model = PetOwner
        fields = ["id", "first_name", "last_name","email","phone", "address", "created_at", "pets"]

## Pet with Owner
class PetOwnerSerializer(serializers.ModelSerializer):
    owner = OwnersListSerializer()
    class Meta:
        model = Pet
        fields = ["id","name","type","created_at","owner"]

### Dates
class DatesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetDate
        fields = ["id","datetime",]

class DatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetDate
        fields = "__all__"

## Dates with pet
class DatesPetSerializer(serializers.ModelSerializer):
    pet = PetsListSerializer(many=True)
    
    class Meta:
        model = PetDate
        fields = ["id", "datime", "type", "created_at", "pet"]

## Lista de oficinas
class OfficesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ['id','name','phone']

class OfficesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = "__all__"

# Dates with offices
class DatesOfficeSerilizer(serializers.ModelSerializer):
    office = OfficesListSerializer()
    pet = PetsListSerializer(many=True)
    class Meta:
        model = PetDate
        fields = ["id", "datime", "type", "created_at", "pet", "office"]


## List Office Detail with Dates -->Error
class OfficeDatesSerializer(serializers.ModelSerializer):
    date = DatesListSerializer()
    class Meta:
        model = Office
        fields = ["id","name","zip_code","address","longitude","latitude","phone","created_at","date"]


## USer

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]
        extra_kwargs = {
            'password':{
                "writte_only": True
            }
        }
    
    def create(self, validate_data):
        print(validate_data)
        user =  User.objects.create_user(**validate_data)

        return user