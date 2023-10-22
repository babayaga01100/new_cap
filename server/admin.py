from django.contrib import admin

from .models import SmartFarmSensor

# Register your models here.
@admin.register(SmartFarmSensor)
class SmartFarmModelAdmin(admin.ModelAdmin):
    pass