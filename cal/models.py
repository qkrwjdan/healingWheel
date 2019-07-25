from django.db import models
from django.shortcuts import reverse

class Income(models.Model):
    name = models.CharField(max_length = 20)
    money = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')


class spending(models.Model):
    name = models.CharField(max_length = 20)
    money = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')
