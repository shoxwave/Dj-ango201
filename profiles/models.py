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

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a new Profile() object when a Django User is created."""
    if created:
        Profile.objects.create(user=instance)

#Post Image model
class Edit(models.Model):
    text = models.CharField(max_length=140, blank=False, null=False)
    image = ImageField()
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField()
    joined_date = models.DateField()



    # user_edit = models.OneToOneField(
    #     User,
    #     on_delete=models.CASCADE,
    #     related_name="profile"
    # )
    def __str__(self):
        return self.text
    
# #Edit model
# class Edit(models.Model):
#     model = Edit
#     fields = ["name"]
#     template_name_suffic = "update_form"