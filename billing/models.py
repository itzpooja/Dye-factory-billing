from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class mt_type(models.Model):
    m_type=models.CharField(max_length=1000, null=True, blank=True)
    mt_price=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.m_type}"

class received_details(models.Model):
    dc_no = models.IntegerField(null=True, blank=True)
    m_name = models.ForeignKey(mt_type, on_delete=models.SET_NULL, null=True)
    m_length = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return f"{self.dc_no}"

class bill(models.Model):
    dc_no=models.ForeignKey(received_details, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.dc_no}"