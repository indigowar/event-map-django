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

    subjects = SubjectSerializer(many=True)

    class Meta:
        model = models.Event
        fields = '__all__'
        read_only_fields = ['id']

    # def create(self, validated_data):
    #     subs = validated_data.pop('subjects')
    #
    #     new_event = models.Event.objects.create(**validated_data)
    #
    #     for s in subs:
    #         subject = models.Subject(subject=s)
    #         subject.save()
