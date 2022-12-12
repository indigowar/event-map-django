from django.db import models


class OrganizerLevel(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=3)

    def __str__(self):
        return '{name} ({code})'.format(name=self.name, code=self.code)


class Organizer(models.Model):
    name = models.CharField(max_length=255)
    logo = models.TextField()
    level = models.ForeignKey(OrganizerLevel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FoundingType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class FoundingRange(models.Model):
    low = models.IntegerField()
    high = models.IntegerField()

    def __str__(self):
        return '({low}-{high})'.format(low=self.low, high=self.high)


class CoFoundingRange(models.Model):
    low = models.IntegerField()
    high = models.IntegerField()

    def __str__(self):
        return '({low}-{high})'.format(low=self.low, high=self.high)


class Competitor(models.Model):
    name = models.CharField(max_length=255)
    code = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Subject(models.Model):
    subject = models.CharField(max_length=255, blank=False)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)

    def __str__(self):
        return self.subject


class Event(models.Model):
    title = models.CharField(max_length=255)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    founding_type = models.ManyToManyField(FoundingType, related_name="event")
    founding_range = models.OneToOneField(FoundingRange, on_delete=models.CASCADE)
    co_founding_range = models.OneToOneField(CoFoundingRange, on_delete=models.CASCADE)
    submission_deadline = models.DateField()
    consideration_period = models.CharField(max_length=255)
    realisation_period = models.CharField(max_length=255)
    result = models.TextField()
    site = models.CharField(max_length=512)
    document = models.CharField(max_length=512)
    internal_contacts = models.CharField(max_length=512)
    trl = models.IntegerField()
    # subjects = models.ManyToManyField(Subject, related_name="event")
    competitors = models.ManyToManyField(Competitor, related_name="event")

    precursor = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    @property
    def subjects(self):
        return Subject.objects.filter(event_id=self.id)

    def __str__(self):
        return self.title
