from django.db import models


class Rota(models.Model):
    session_date = models.DateTimeField()
    session_name = models.CharField(max_length=120)
    session_start_time = models.TimeField()
    session_lead = models.CharField(max_length=120)
