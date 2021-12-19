from django.db import models


# Create your models here.
class Computer(models.Model):
    name = models.CharField(max_length=256, verbose_name="Computer name")
    model = models.CharField(max_length=256, verbose_name="Computer model")

    def __str__(self):
        return self.name


class Browser(models.Model):
    name = models.CharField(max_length=256, verbose_name="Browser name")
    memory_on_disk = models.PositiveIntegerField(verbose_name="Browser memory on disk")
    comp_browser = models.ForeignKey(
        Computer,
        on_delete=models.SET_DEFAULT,
        null=True,
        default=None,
        related_name="browsers"
    )

    def __str__(self):
        return self.name
