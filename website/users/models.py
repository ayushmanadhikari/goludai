from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/', default="default.jpg")

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height >300 or img.width >300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


