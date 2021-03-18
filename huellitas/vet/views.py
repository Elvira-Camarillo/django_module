from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import View, TemplateView, DetailView

from .models import PetOwner, Pet

# Create your views here.

class Owners(View):
    def get(self, request):
        """List owners."""
        owners = PetOwner.objects.all()
        context = {"owners": owners}

        template = loader.get_template("vet/owners/list.html")
        return HttpResponse(template.render(context, request))

class OwnersList(TemplateView):
    template_name = 'vet/owners/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owners'] = PetOwner.objects.all()
        return context


class OwnersDetail(DetailView):
    model = PetOwner
    template_name = 'vet/owners/detail.html'
    context_object_name='owner'


class PetsList(View):
    def get(self, request):
        pets = Pet.objects.all()
        context = {"pets":pets}
        
        template = loader.get_template("vet/pets/listPets.html")
        return HttpResponse(template.render(context, request))



class Test(View):
    def get(self, request):
        return HttpResponse('Hola Mundo desde Clase View')