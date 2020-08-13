from django.db import models


class details(models.Model):
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=15)
    phone_no = models.IntegerField()
    gender = models.CharField(max_length=10)

