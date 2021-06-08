from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver


UserModel = get_user_model()

@receiver(post_save, sender=UserModel)
def profile_create(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=UserModel)
def profile_create(sender, instance, **kwargs):
    instance.profile.save()