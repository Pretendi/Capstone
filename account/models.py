from django.db import models
from django.contrib.auth.models	import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class SurveyID(models.Model):
	question1 = models.TextField()
	question2 = models.TextField()
	question3 = models.TextField()
	question4 = models.TextField()

"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
"""