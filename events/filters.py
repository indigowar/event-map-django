import django_filters
from django.db.models import QuerySet

from events import models

"""""
```json
{
    "subjects": [
        id1,
        id2,
        ...
    ],
    "competitors": [
        id1,
        id2,
        ...
    ],
    "founding_range": {
        "low": 0,
        "high": 100
    },
    "co_founding_range": {
        "low": 0,
        "high": 15
    },
    "founding_type": [
        id1,
        id2,
        id3
    ].
    "submission_deadline": {
        "start": "YYYY-MM-DD",
        "end": "YYYY-MM-DD"
    },
    "trl": [
        ...
    ],
}
```
"""


def __filtrate_event_by_subjects(q: QuerySet, subjects: list[str]) -> QuerySet:
    event_ids = [s.event_id for s in models.Subject.objects.filter(subject__in=subjects)]
    return q.filter(pk__in=event_ids)


def __filtrate_event_by_competitors(q: QuerySet, competitors: list[int]) -> QuerySet:
    return q.filter(competitors__in=competitors)


def __filtrate_event_by_trl(q: QuerySet, trl: list[int]) -> QuerySet:
    return q.filter(trl__in=trl)


def __filtrate_event_by_founding_range(q: QuerySet, data: dict) -> QuerySet:
    if 'low' in data.keys():
        low = data['low']
        q = q.filter(founding_range__low__gte=low)
    if 'high' in data.keys():
        high = data['high']
        q = q.filter(founding_range__high__lte=high)
    return q


def __filtrate_event_by_co_founding_range(q: QuerySet, data: dict) -> QuerySet:
    if 'low' in data.keys():
        low = data['low']
        q = q.filter(co_founding_range__low__gte=low)
    if 'high' in data.keys():
        high = data['high']
        q = q.filter(co_founding_range__high__lte=high)
    return q


# TODO: implement
def __filtrate_event_by_submission_deadline(q: QuerySet, d: dict) -> QuerySet:
    if 'start' in d.keys():
        start_date = d['start']
        q = q.filter(submission_deadline__gte=start_date)
    if 'end' in d.keys():
        end_date = d['end']
        q = q.filter(submission_deadline__lte=end_date)
    return q


def filtrate_event(data: dict) -> QuerySet:
    queryset = models.Event.objects.all()

    if 'subjects' in data.keys():
        queryset = __filtrate_event_by_subjects(queryset, data['subjects'])

    if 'competitors' in data.keys():
        queryset = __filtrate_event_by_competitors(queryset, data['competitors'])

    if 'trl' in data.keys():
        queryset = __filtrate_event_by_trl(queryset, data['tlr'])

    if 'founding_range' in data.keys():
        queryset = __filtrate_event_by_founding_range(queryset, data['founding_range'])

    if 'co_founding_range' in data.keys():
        queryset = __filtrate_event_by_co_founding_range(queryset, data['co_founding_range'])

    if 'submission_deadline' in data.keys():
        queryset = __filtrate_event_by_submission_deadline(queryset, data['submission_deadline '])

    return queryset


class EventFilter(django_filters.FilterSet):
    id = django_filters.AllValuesMultipleFilter()

    # filtering by organizer's level
    organizer_level = django_filters.ModelMultipleChoiceFilter(field_name='organizer__level',
                                                               queryset=models.OrganizerLevel.objects.all())

    # filters that low should be greater than given and high should be lesser
    f_range_min = django_filters.NumberFilter(field_name='founding_range__low', lookup_expr='gte')
    f_range_max = django_filters.NumberFilter(field_name='founding_range__high', lookup_expr='lte')

    cf_range_min = django_filters.NumberFilter(field_name='co_founding_range__low', lookup_expr='gte')
    cf_range_max = django_filters.NumberFilter(field_name='co_founding_range__high', lookup_expr='lte')

    founding_type = django_filters.ModelMultipleChoiceFilter(field_name='founding_type',
                                                             queryset=models.FoundingType.objects.all())

    competitors = django_filters.ModelMultipleChoiceFilter(field_name='competitors',
                                                           queryset=models.Competitor.objects.all())

    submission_deadline = django_filters.DateRangeFilter(field_name='submission_deadline')

    trl = django_filters.AllValuesMultipleFilter()

    class Meta:
        model = models.Event
        fields = ['organizer']
