from django.db.models import QuerySet

from events import models


class EventFilterData:
    def __init__(self, data: dict):
        pass

    def is_valid(self) -> (bool, str):
        return True, "event filter data is empty"


class EventFilter:
    def filtrate(self, data: EventFilterData) -> QuerySet:
        return models.Event.objects.all()
