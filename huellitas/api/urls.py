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
RetrievePetsOwnerAPIView,
ListDatesAPIView,
CreateDatesAPIView,
RetrieveDatesAPIView,
UpdateDatesListAPIView,
DestroyDatesListAPIView,
RetrieveDatesPetAPIView,
ListOfficesAPIView,
CreateOfficesAPIView,
RetrieveOfficesAPIView,
RetrieveOfficeDatesAPIView,
RetrieveDatesOfficeAPIView,
RetriveUpdatePetsAPIView,
CreateUsersAPIView
)

urlpatterns = [
    path("users/create", CreateUsersAPIView.as_view(),name="create-user"),
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
    ##  PetDates
    path("dates/", ListDatesAPIView.as_view(),name="list-dates"),
    path("dates/create/", CreateDatesAPIView.as_view(),name="create-dates"),
    path("dates/<int:pk>/", RetrieveDatesAPIView.as_view(),name="retrieve-dates"),
    #path("dates/<int:pk>/", RetrieveDatesOfficeAPIView.as_view(),name="retrieve-dates-office"),
    path("dates/<int:pk>/update", UpdateDatesListAPIView.as_view(),name="update-dates"),
    path("dates/<int:pk>/destroy", DestroyDatesListAPIView.as_view(),name="destroy-dates"),
    path("dates/<int:pk>/pets", RetrieveDatesPetAPIView.as_view(),name="retrieve-dates-pet"),
    ## Offices
    path("offices/", ListOfficesAPIView.as_view(),name="list-offices"),
    path("offices/create/", CreateOfficesAPIView.as_view(),name="create-offices"),
    path("offices/<int:pk>/", RetrieveOfficesAPIView.as_view(),name="retrieve-offices"),
    path("offices/<int:pk>/dates",RetrieveOfficeDatesAPIView.as_view(),name="retrieve-office-dates"),


     path("pets/<int:pk>/list-update", RetriveUpdatePetsAPIView.as_view(),name="retrive-update-pets"),
]

