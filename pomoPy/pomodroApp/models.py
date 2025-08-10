""" from django.db import models
import datetime
from zoneinfo import ZoneInfo 
from datetime import timedelta

plusFifty = datetime.datetime.now(ZoneInfo("Asia/Kolkata")) + timedelta(minutes=50)
plus25 = datetime.datetime.now(ZoneInfo("Asia/Kolkata")) + timedelta(minutes=25)

class PomoModel(models.Model):
    time_model50 = models.DateTimeField(default=plusFifty)
    time_model25 = models.DateTimeField(default=plus25)


 """