from django.db import models


class Acceleration(models.Model):
    device_id = models.CharField(max_length=255)
    acceleration = models.DecimalField(max_digits=8, decimal_places=4)
    timestamp = models.DateTimeField()
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'acceleration'
