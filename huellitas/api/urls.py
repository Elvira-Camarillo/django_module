from django.urls import path, include
from rest_framework import routers
from .views import OwnersViewSet, PetsViewSet,PetDateViewSet

router = routers.DefaultRouter()
router.register(r"owners",OwnersViewSet)
router.register(r"pets",PetsViewSet)
router.register(r"petdate",PetDateViewSet)

urlpatterns = [
    path("", include(router.urls)),
]