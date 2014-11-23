from rest_framework import serializers
import data.models as models


class AccelerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Acceleration
        fields = ('device_id', 'accelerometer', 'timestamp')
