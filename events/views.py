import django.db.models
from django.http import HttpRequest, HttpResponse, JsonResponse

from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.parsers import JSONParser

from events import serializers, models, filters


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
    serializer_class = serializers.EventSerializer

    parser_classes = [JSONParser]

    def get_queryset(self):
        data = filters.EventFilterData(self.request.data)
        valid, err = data.is_valid()
        if not valid:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'error': err})
        return filters.EventFilter().filtrate(data=data)

# @api_view(['GET'])
# @parser_classes([JSONParser])
# @permission_classes((permissions.AllowAny,))
# def filtering_events_view(request: HttpRequest) -> HttpResponse:
#     data = filters.EventFilterData(request.data)
#     valid, err = data.is_valid()
#     if not valid:
#         return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'message': err})
#     events = filters.EventFilter().filtrate(data)
#
#     if len(events) > 0:
#         if len(events) == 1:
#             serializer = serializers.EventSerializer(events)
#             return JsonResponse(status=status.HTTP_200_OK, data=serializer.initial_data)
#         serializer = serializers.EventSerializer(data=events, many=True)
#         return JsonResponse(status=status.HTTP_200_OK, data=serializer.initial_data, safe=False)
#     return JsonResponse(status=status.HTTP_404_NOT_FOUND, data={'message': 'nothing was found with this filters'})
