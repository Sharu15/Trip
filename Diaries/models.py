from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateField(default=timezone.now)
	
	def __str__(self):
		return self.title

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return f"{self.post.title}|{self.text[:30]}"

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200,blank=True)
	last_name = models.CharField(max_length=200,blank=True)
	username = models.CharField(max_length=200)
	dob = models.DateField(blank=True, null=True)
	email = models.EmailField(max_length=70,blank=True)
	phone_number = models.CharField(max_length=12)


	def __str__(self):
		return f"{self.username}" 

class Plan(models.Model):
	created_date = models.DateTimeField(auto_now_add=True)
	place = models.CharField(max_length=200)
	start_date = models.DateField()
	end_date = models.DateField() 
	schedule = models.TextField() #day event
	to_do_list = models.TextField() #things to do

	def __str__(self):
		return f"{self.place}|{self.start_date}"


