from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta


class DrivingTime(models.Model):
    # user = models.OneToOneField(User,on_delete = models.CASCADE, related_name='' )
    MENU_1 = '10'
    MENU_2 = '30'
    MENU_3 = '60'

    VOUCHER_CHOICES = [
        (MENU_1,'10분'),
        (MENU_2,'20분'),
        (MENU_3,'30분'),
    ]
    detail_menu = models.CharField(
        max_length = 10,
        choices = VOUCHER_CHOICES,
        default = MENU_1,
    )

    duration = models.DurationField(default = timedelta(0))
