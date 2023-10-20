from django.db import models

# Create your models here.
class SmartFarm(models.Model):
    sfid = models.IntegerField
    remotepower = models.BooleanField
    temperature = models.FloatField
    humidity = models.FloatField
    light = models.IntegerField
    soil = models.IntegerField
    
    ledpower = models.BooleanField
    ledstate = models.BooleanField
    ledtoggle = models.BooleanField
    ledautotoggle = models.BooleanField
    ledstarttimevalue = models.IntegerField
    ledstartminutevalue = models.IntegerField
    ledendtimevalue = models.IntegerField
    ledendminutevalue = models.IntegerField
    
    water_pump_power = models.BooleanField
    water_pump_state = models.BooleanField
    water_pump_toggle = models.BooleanField
    water_pump_auto_toggle = models.BooleanField
    water_pump_start_time = models.IntegerField
    water_pump_running_time = models.IntegerField
    water_level_voltage = models.FloatField
    water_temperature = models.FloatField
    
    
    fan_power = models.BooleanField
    fan_state = models.BooleanField
    fan_toggle = models.BooleanField
    fan_auto_toggle = models.BooleanField
    fan_start_time_value = models.IntegerField
    fan_start_minute_value = models.IntegerField
    fan_end_time_value = models.IntegerField
    fan_end_minute_value = models.IntegerField

    door_power = models.BooleanField
    door_state = models.BooleanField
    door_toggle = models.BooleanField
    door_auto_toggle = models.BooleanField
    door_start_time_value = models.IntegerField
    door_start_minute_value = models.IntegerField
    door_end_time_value = models.IntegerField
    door_end_minute_value = models.IntegerField
    
    waterlevelwarning = models.TextField
    watertempwarning = models.TextField
    tempwarning = models.TextField
    humwarning = models.TextField
    soilwarning = models.TextField