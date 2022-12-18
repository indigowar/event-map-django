import django_filters

from events import models


class OrganizerFilter(django_filters.FilterSet):
    class Meta:
        model = models.Organizer
        fields = ['id']


class EventFilter(django_filters.FilterSet):
    id = django_filters.AllValuesMultipleFilter()
    organizer = django_filters.ModelMultipleChoiceFilter(field_name='organizer',
                                                         queryset=models.Organizer.objects.all())

    # filtering by organizer's level
    organizer_level = django_filters.ModelMultipleChoiceFilter(field_name='organizer__level',
                                                               queryset=models.OrganizerLevel.objects.all())

    # filters that low should be greater than given and high should be lesser
    f_range_min = django_filters.NumberFilter(field_name='founding_range__low', lookup_expr='gte')
    f_range_max = django_filters.NumberFilter(field_name='founding_range__high', lookup_expr='lte')

    cf_range_min = django_filters.NumberFilter(field_name='co_founding_range__low', lookup_expr='gte')
    cf_range_max = django_filters.NumberFilter(field_name='co_founding_range__high', lookup_expr='lte')

    founding = django_filters.ModelMultipleChoiceFilter(field_name='founding_type',
                                                        queryset=models.FoundingType.objects.all())

    competitors = django_filters.ModelMultipleChoiceFilter(field_name='competitors',
                                                           queryset=models.Competitor.objects.all())

    submission_deadline = django_filters.DateFromToRangeFilter(field_name='submission_deadline')

    trl = django_filters.AllValuesMultipleFilter()

    class Meta:
        model = models.Event
        fields = []
