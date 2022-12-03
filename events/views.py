from django_filters import rest_framework

from rest_framework import generics
from rest_framework.parsers import JSONParser

from events import serializers, filters
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


class EventListAndCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer


class EventRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer


class EventFilterListAPIView(generics.ListAPIView):
    """
    On GET returns a filtered list of events:

    Request body: https://github.com/indigowar/event-map-django

    """
    serializer_class = serializers.EventSerializer

    parser_classes = [JSONParser]

    def get_queryset(self):
        return filters.filtrate_event(self.request.data)
