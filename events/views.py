from django_filters import rest_framework as filters

from rest_framework import generics, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser
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
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class FavoriteListAPIView(viewsets.ModelViewSet):
    queryset = models.FavoriteList.objects.all()
    serializer_class = serializers.FavoriteListSerializer
    permission_classes = (IsAuthenticated, IsObjectOwner)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.filter(user=self.request.user).first()
        return obj

    def create(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj:
            raise PermissionDenied("Favorite list already exists for this user.")
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_vali(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
