from rest_framework import serializers

from events import models


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
        founding_type = vd.pop('founding_range')

        event = models.Event.objects.create(**vd, founding_range=founding_range,
                                            co_founding_range=co_founding_range, founding_type=founding_type)

        event.competitors.set(competitors)
        event.founding_type.set(founding_type)

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
