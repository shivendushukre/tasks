from django.db import models
from django.contrib.auth.models import User


class profile(models.Model):
    phone_no = models.IntegerField()
    phone = models.OneToOneField(User, max_length=15, on_delete=models.CASCADE)

    






