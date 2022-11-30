from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class CustomUser(AbstractUser):
    def __str__(self):
        return self.username



class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile_user")
    avatar = models.ImageField(upload_to="profile/", blank=True, null=True)
    phone_validators = RegexValidator(regex=[r'\?0?+{9,15}$'], message="Please Enter a valid phone number")
    phone = models.CharField(_("Contact Phone"), validators=[phone_validators], null=True, blank=True, max_length=15)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.first_name}" or f"{self.user}"
    
    @receiver(post_save, sender=CustomUser)
    def profile_post_save_receiver(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        
    
        
    

