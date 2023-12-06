from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Lead(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField(default=10)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organistaion = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.user.username

# Here we actually create user model and connct to post_save that would be available to the Agent.
def post_user_created_signal(sender, instance, created, **kwargs):
    print(instance)
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)         #here the sender is the model which is used to sent i.e, the User model.
