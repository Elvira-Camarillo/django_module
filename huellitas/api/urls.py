from django.urls import path, include

from .views import (ListOwnersAPIView, 
RetrieveOwnersAPIView, 
CreateOwnersAPIView, 
ListPetsAPIView, 
RetrievePetsAPIView, 
CreatePetsAPIView, 
UpdateOwnersListAPIView, 
UpdatePetsListAPIView, 
DestroyOwnersListAPIView, 
DestroyPetsListAPIView,
RetrieveOwnerPetsAPIView,
RetrievePetsOwnerAPIView
)

urlpatterns = [
    path("owners/", ListOwnersAPIView.as_view(),name="list-owners"),
    path("owners/create/", CreateOwnersAPIView.as_view(),name="create-owners"),
    path("owners/<int:pk>/", RetrieveOwnersAPIView.as_view(),name="retrieve-owners"),
    path("owners/<int:pk>/update", UpdateOwnersListAPIView.as_view(),name="update-owners"),
    path("owners/<int:pk>/destroy", DestroyOwnersListAPIView.as_view(),name="destroy-owners"),
    path("owners/<int:pk>/pets", RetrieveOwnerPetsAPIView.as_view(),name="retrieve-owner-pets"),
    path("pets/", ListPetsAPIView.as_view(),name="list-pets"),
    path("pets/create/", CreatePetsAPIView.as_view(),name="create-pets"),
    ## path("pets/<int:pk>/", RetrievePetsAPIView.as_view(),name="retrieve-pets"),
    path("pets/<int:pk>/update", UpdatePetsListAPIView.as_view(),name="update-pets"),
    path("pets/<int:pk>/destroy", DestroyPetsListAPIView.as_view(),name="destroy-pets"),
    path("pets/<int:pk>/", RetrievePetsOwnerAPIView.as_view(),name="retrieve-pets-owner"),
]

