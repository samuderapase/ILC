from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):	
	writer = models.ForeignKey(User)
	name_post = models.CharField(max_length=200)
	content = models.TextField()
	date_post = models.DateTimeField(auto_now_add=True)
	
	
class Author(models.Model):
    user_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)	
    last_name = models.CharField(blank=True, help_text="not required", max_length=50)
    phone = models.CharField(help_text="example +62 85270546829", max_length=20)
    email = models.EmailField()
    website = models.URLField(help_text="not required", blank=True)
	
class Schedule(models.Model):
	schedule = models.CharField(max_length=200)
	trainer_name = models.CharField(max_length=200)
	date_schedule = models.DateTimeField()
	description = models.TextField(blank=True)
		
