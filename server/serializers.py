from rest_framework.serializers import ModelSerializer

from .models import SmartFarm

class SmartFarmBaseModelSerializer(ModelSerializer):
    class Meta:
        model = SmartFarm
        fields = '__all__'
        # exclude = ("")

class InfoListModelSerializer(SmartFarmBaseModelSerializer):
    class Meta(SmartFarmBaseModelSerializer.Meta):
        fields = ['id', 
                  'sfid', 
                  'remotepower', 
                  'remperature', 
                  'humidity']
        
class LedListModelSerializer(SmartFarmBaseModelSerializer):
    class Meta(SmartFarmBaseModelSerializer.Meta):
        fields = ['ledpower', 
                  'ledstate', 
                  'ledtoggle', 
                  'ledautotoggle', 
                  'ledstarttimevalue', 
                  'ledstartminutevalue', 
                  'ledendtimevalue', 
                  'ledendminutevalue']
        
class WaterListModelSerializer(SmartFarmBaseModelSerializer):
    class Meta(SmartFarmBaseModelSerializer.Meta):
        filed = ['water_pump_power',
                'water_pump_state',
                'water_pump_toggle',
                'water_pump_auto_toggle',
                'water_pump_start_time',
                'water_pump_running_time',
                'water_level_voltage',
                'water_temperature']
class FanListModelSerializer(SmartFarmBaseModelSerializer):
    class Meta(SmartFarmBaseModelSerializer.Meta):
        field = [
            'fan_power',
            'fan_state',
            'fan_toggle',
            'fan_auto_toggle',
            'fan_start_time_value',
            'fan_start_minute_value',
            'fan_end_time_value',
            'fan_end_minute_value'
        ]
        
class DoorListModelSerializer(SmartFarmBaseModelSerializer):
    class Meta(SmartFarmBaseModelSerializer.Meta):
        field = [
                'door_power',
                'door_state',
                'door_toggle',
                'door_auto_toggle',
                'door_start_time_value',
                'door_start_minute_value',
                'door_end_time_value',
                'door_end_minute_value'
        ]
        
class WarningListModelSerializer(SmartFarmBaseModelSerializer):
    class Meta(SmartFarmBaseModelSerializer.Meta):
        field = [
                'waterlevelwarning',
                'watertempwarning',
                'tempwarning',
                'humwarning',
                'soilwarning'
        ]