from django.contrib import admin

from cap.server.models import SmartFarm

# Register your models here.
@admin.register(SmartFarm)
class SmartFarmModelAdmin(admin.ModelAdmin):
    pass