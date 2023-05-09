from django_filters import rest_framework as filters

from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated, BasePermission
from rest_framework.response import Response

from events import serializers, models
from events.filters import EventFilter


class GeneralModelViewSet(viewsets.ModelViewSet):
    """
    The general view set for models.


    GET methods(List and Retrieve) can be used without authentication,
    but all others(Create, Update,Delete) can be used only by authenticated users.
    """

    permission_classes = (IsAdminUser,)

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = []
        return super(viewsets.ModelViewSet, self).get_permissions()


class OrganizerViewSet(GeneralModelViewSet):
    queryset = models.Organizer.objects.all()
    serializer_class = serializers.OrganizerSerializer


class OrganizerLevelViewSet(GeneralModelViewSet):
    queryset = models.OrganizerLevel.objects.all()
    serializer_class = serializers.OrganizerLevelSerializer


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


class IsObjectOwner(BasePermission):
    """
    Custom permission to check if the authenticated user is the owner of the object in question
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class FavoriteListAPIView(viewsets.ModelViewSet):
    queryset = models.FavoriteList.objects.all()
    serializer_class = serializers.FavoriteListSerializer

    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.queryset.filter(user=request.user.id)
        serializer = self.serializer_class(data=instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
