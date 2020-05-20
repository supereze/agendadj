from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)
from .models import Person, Reunion
from .serializers import (
    PersonSerializer,
    PersonaSerializer,
    PersonaSerializer2,
    PersonaSerializer3,
    ReunionSerializer,
    ReunionSerializerLink
)


class ListaPersonas(ListView):
    template_name = "persona/personas.html"
    context_object_name = 'personas'

    def get_queryset(self):
        return Person.objects.all()
    

class PersonListApiView(ListAPIView):

    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()


class PersonListView(TemplateView):
    template_name = "persona/original.html"


class PersonSearchApiView(ListAPIView):

    serializer_class = PersonSerializer

    def get_queryset(self):
        kword = self.kwargs['kword']
        return Person.objects.filter(
            full_name__icontains=kword
        )


class PersonCreateView(CreateAPIView):

    serializer_class = PersonSerializer


class PersonDetailView(RetrieveAPIView):

    serializer_class = PersonSerializer
    queryset = Person.objects.filter()


class PersonDeleteView(DestroyAPIView):

    serializer_class = PersonSerializer
    queryset = Person.objects.filter()


class PersonUpdateView(UpdateAPIView):

    serializer_class = PersonSerializer
    queryset = Person.objects.filter()


class PersonRetriveUpdateView(RetrieveUpdateAPIView):

    serializer_class = PersonSerializer
    queryset = Person.objects.filter()


class PersonApiLista(ListAPIView):

    #serializer_class = PersonaSerializer
    serializer_class = PersonaSerializer3

    def get_queryset(self):
        return Person.objects.all()


class ReunionApiLista(ListAPIView):

    serializer_class = ReunionSerializer

    def get_queryset(self):
        return Reunion.objects.all()


class ReunionApiListaLink(ListAPIView):

    serializer_class = ReunionSerializerLink

    def get_queryset(self):
        return Reunion.objects.all()