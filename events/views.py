from django_filters import rest_framework as filters

from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from events import serializers, models
from events.filters import EventFilter


class GeneralModelViewSet(viewsets.ModelViewSet):
    """
    The general view set for models.


    GET methods(List and Retrieve) can be used without authentication,
    but all others(Create, Update,Delete) can be used only by authenticated users.
    """

    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = []
        return super(viewsets.ModelViewSet, self).get_permissions()


class OrganizerViewSet(GeneralModelViewSet):
    queryset = models.Organizer.objects.all()
    serializer_class = serializers.OrganizerSerializer


class CompetitorViewSet(GeneralModelViewSet):
    queryset = models.Competitor.objects.all()
    serializer_class = serializers.CompetitorSerializer


class FoundingTypeViewSet(GeneralModelViewSet):
    queryset = models.FoundingType.objects.all()
    serializer_class = serializers.FoundingTypeSerializer


class EventViewSet(GeneralModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EventFilter


class SubjectListAPIView(generics.ListAPIView):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer


class MinimalEventListAPIView(viewsets.ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.MinimalEventSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EventFilter


class EventForPrintingListAPIView(viewsets.ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventNestedSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EventFilter
