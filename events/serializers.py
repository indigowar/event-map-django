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

    def create(self, vd):
        subjects = vd.pop('subjects')

        founding_range = FoundingRangeSerializer().create(validated_data=vd.pop('founding_range'))
        co_founding_range = CoFoundingRangeSerializer().create(validated_data=vd.pop('co_founding_range'))

        competitors = vd.pop('competitors')

        event = models.Event.objects.create(**vd, founding_range=founding_range,
                                            co_founding_range=co_founding_range)

        event.competitors.set(competitors)
        event.save()

        for subject in subjects:
            subject_model = models.Subject(subject=subject, event_id=event.id)
            subject_model.save()

        return event
