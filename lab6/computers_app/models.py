from django.db import models


# Create your models here.
class Computer(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название компьютера")
    cost = models.IntegerField(verbose_name="Стоимость компьютера")
    description = models.CharField(max_length=255, verbose_name="Описание компьютера")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="Когда последний раз обновлялась информация о "
                                                                     "компьютере?")
