import django_filters

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
