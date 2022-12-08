from django_filters import rest_framework as filters

from rest_framework import generics, viewsets
from rest_framework.parsers import JSONParser

from events import serializers
from events.filters import *


class OrganizerLevelListAPIView(generics.ListAPIView):
    queryset = models.OrganizerLevel.objects.all()
    serializer_class = serializers.OrganizerLevelSerializer


class OrganizerListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Organizer.objects.all()
    serializer_class = serializers.OrganizerSerializer


class OrganizerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Organizer.objects.all()
    serializer_class = serializers.OrganizerSerializer


class CompetitorListAPIView(generics.ListAPIView):
    queryset = models.Competitor.objects.all()
    serializer_class = serializers.CompetitorSerializer


class FoundingTypeListAPIView(generics.ListAPIView):
    queryset = models.FoundingType.objects.all()
    serializer_class = serializers.FoundingTypeSerializer


class EventListAndCreateAPIView(viewsets.ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EventFilter


class EventRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer


class CompetitorListAndCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Competitor.objects.all()
    serializer_class = serializers.CompetitorSerializer


class CompetitorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Competitor.objects.all()
    serializer_class = serializers.CompetitorSerializer


class SubjectListAPIView(generics.ListAPIView):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer


class FoundingTypeListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.FoundingType.objects.all()
    serializer_class = serializers.FoundingTypeSerializer


class FoundingTypeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.FoundingType.objects.all()
    serializer_class = serializers.FoundingTypeSerializer
