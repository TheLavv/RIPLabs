from django.db import models


# Create your models here.
class Computer(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    description = models.CharField(max_length=232)


class Browser(models.Model):
    name = models.CharField(max_length=255)
    memory_on_disk = models.PositiveIntegerField()
    computer_id = models.IntegerField()
    description = models.CharField(max_length=255)