from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    image = ImageField(upload_to='profiles')
    firstname = models.CharField(max_length=255, blank=False, null=False)
    lastname = models.CharField(max_length=255, blank=False, null=False)
    username = models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a new Profile() object when a Django User is created."""
    if created:
        Profile.objects.create(user=instance)    

#Post Image model
class Post(models.Model):
    text = models.CharField(max_length=100, blank=False, null=False)
    image = ImageField()
    
    def __str__(self):
        return self.text