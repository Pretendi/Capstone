from django.db import models
from django.contrib.auth.models	import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class SurveyID(models.Model):
	surveyID = models.AutoField(primary_key=True)
	userID = models.ForeignKey(User, on_delete=models.CASCADE)
	age = models.IntegerField()
	gender = models.CharField(max_length=2)
	status = models.CharField(max_length=2)
	investment = models.CharField(max_length=2)
	combination = models.CharField(max_length=2)

"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
"""