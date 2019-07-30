from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    duration = models.DurationField(default = timedelta(0))

    @receiver(post_save, sender = User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender = User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username


class DrivingTime(models.Model):
    MENU_1 = '10'
    MENU_2 = '30'
    MENU_3 = '60'

    VOUCHER_CHOICES = [
        (MENU_1,'10분'),
        (MENU_2,'30분'),
        (MENU_3,'60분'),
    ]
    detail_menu = models.CharField(
        max_length = 10,
        choices = VOUCHER_CHOICES,
        default = MENU_1,
    )
