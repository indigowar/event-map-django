from django.contrib import admin

from events import models

# Register your models here.

admin.site.register(models.Event)
admin.site.register(models.Competitor)
admin.site.register(models.Subject)
admin.site.register(models.OrganizerLevel)
admin.site.register(models.Organizer)
admin.site.register(models.FoundingRange)
admin.site.register(models.CoFoundingRange)
admin.site.register(models.FoundingType)
admin.site.register(models.FavoriteList)
