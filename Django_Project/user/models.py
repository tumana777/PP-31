from django.contrib.auth.models import User
from django.db import models


# class CustomUser(AbstractUser):
#     pass

class UserProfile(models.Model):
    phone_number = models.CharField(max_length=140, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    class Meta:
        db_table = 'user_profiles'
        verbose_name = 'user profile'
        verbose_name_plural = 'user profiles'

    def __str__(self):
        return f"{self.user.username}'s profile"