from django.db import models


class Crud(models.Model):
    nama = models.CharField(max_length=100)
    motto = models.TextField()
