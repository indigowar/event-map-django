from rest_framework import serializers

from events import models


class RelatedFieldAlternative(serializers.PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = kwargs.pop('serializer', None)
        if self.serializer is not None and not issubclass(self.serializer, serializers.Serializer):
            raise TypeError('"serializer" is not a valid serializer class')

        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False if self.serializer else True

    def to_representation(self, instance):
        if self.serializer:
            return self.serializer(instance, context=self.context).data
        return super().to_representation(instance)


class OrganizerLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrganizerLevel
        fields = '__all__'
        read_only_fields = ['id']


class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organizer
        fields = '__all__'
        read_only_fields = ['id']


class FoundingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FoundingType
        fields = '__all__'
        read_only_fields = ['id']


class FoundingRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FoundingRange
        fields = '__all__'
        read_only_fields = ['id']


class CoFoundingRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CoFoundingRange
        fields = '__all__'
        read_only_fields = ['id']


class CompetitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Competitor
        fields = '__all__'
        read_only_fields = ['id']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = '__all__'
        read_only_fields = ['id']


class EventSerializer(serializers.ModelSerializer):
    founding_range = FoundingRangeSerializer()
    co_founding_range = CoFoundingRangeSerializer()

    subjects = serializers.ListSerializer(child=serializers.CharField())

    class Meta:
        model = models.Event
        fields = '__all__'
        read_only_fields = ['id']

    @staticmethod
    def __create_subjects(subs: list[str], event: int):
        for s in subs:
            models.Subject(event_id=event, subject=s).save()

    def create(self, vd):
        subjects = vd.pop('subjects')

        founding_range = FoundingRangeSerializer().create(validated_data=vd.pop('founding_range'))
        co_founding_range = CoFoundingRangeSerializer().create(validated_data=vd.pop('co_founding_range'))

        competitors = vd.pop('competitors')
        f_types = vd.pop('founding_type')

        event = models.Event.objects.create(**vd, founding_range=founding_range,
                                            co_founding_range=co_founding_range)
        event.save()

        event.competitors.set(competitors)
        event.founding_type.set(f_types)

        event.save()

        self.__create_subjects(subjects, event.id)

        return event

    def update(self, instance, validated_data):
        subjects = validated_data.pop('subjects')

        # update ranges

        founding_range_data = validated_data.pop('founding_range')
        founding_range_instance = FoundingRangeSerializer().update(instance=instance.founding_range,
                                                                   validated_data=founding_range_data)

        co_founding_range_data = validated_data.pop('co_founding_range')
        co_founding_range_instance = CoFoundingRangeSerializer().update(instance=instance.co_founding_range,
                                                                        validated_data=co_founding_range_data)

        # co_founding_range = CoFoundingRangeSerializer().update(validated_data=validated_data.pop('co_founding_range'))
        event = super(EventSerializer, self).update(instance, validated_data)
        event.founding_range = founding_range_instance
        event.co_founding_range = co_founding_range_instance
        event.save()

        # update subjects
        models.Subject.objects.filter(event_id=event.id).delete()
        self.__create_subjects(subjects, event.id)

        return event


class MinimalEventSerializer(serializers.ModelSerializer):
    """
    This serializer is required by front-end and does not really have usage anywhere but one view
    """

    class organizer(serializers.ModelSerializer):
        level = serializers.SlugRelatedField(read_only=True, slug_field='code')

        class Meta:
            model = models.Organizer
            fields = ['logo', 'level']

    class foundingRange(serializers.ModelSerializer):
        class Meta:
            model = models.FoundingRange
            fields = ['low', 'high']

    class coFoundingRange(serializers.ModelSerializer):
        class Meta:
            model = models.CoFoundingRange
            fields = ['low', 'high']

    organizer = organizer()
    competitors = serializers.SlugRelatedField(many=True, read_only=True, slug_field='code')
    founding_type = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    founding_range = foundingRange()
    co_founding_range = coFoundingRange()

    class Meta:
        model = models.Event
        fields = [
            'id', 'title', 'organizer',
            'founding_range', 'co_founding_range',
            'founding_type', 'submission_deadline',
            'realisation_period', 'competitors',
            'trl'
        ]


class EventNestedSerializer(serializers.ModelSerializer):
    class foundingRange(serializers.ModelSerializer):
        class Meta:
            model = models.FoundingRange
            fields = ['low', 'high']

    class coFoundingRange(serializers.ModelSerializer):
        class Meta:
            model = models.CoFoundingRange
            fields = ['low', 'high']

    class organizer(serializers.ModelSerializer):
        level = serializers.SlugRelatedField(read_only=True, slug_field='code')

        class Meta:
            model = models.Organizer
            fields = ['logo', 'level', 'name']

    class precursorSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.Event
            fields = ['id', 'title', 'site']

    organizer = organizer()
    competitors = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    founding_type = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    founding_range = foundingRange()
    co_founding_range = coFoundingRange()

    subjects = serializers.ListSerializer(child=serializers.CharField())

    precursor = RelatedFieldAlternative(queryset=models.Event.objects.all(), serializer=precursorSerializer)

    class Meta:
        model = models.Event
        fields = '__all__'
        read_only_fields = ['id']
