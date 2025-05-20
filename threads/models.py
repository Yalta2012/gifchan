from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	treadsCount = models.IntegerField(default=0)
	messagesCount = models.IntegerField(default=0)
	description = models.TextField(default="description")
	def __str__(self):
		return self.title
	

class Thread(models.Model):
	title = models.CharField(max_length=200)
	board = models.ForeignKey(Board, on_delete=models.CASCADE)
	text = models.TextField()
	author = models.ForeignKey(User, default=None,on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(upload_to='images/', blank=True)
	def __str__(self):
		return "thread " + str(self.id)
	def snippet(self):
			return self.text[0:50]+('...' if len(self.text)>50 else "")
	
class Message(models.Model):
	text = models.TextField()
	thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(upload_to='images/', blank=True)
	prev_message = models.ForeignKey('self', null=True, blank=True, default=None,  on_delete=models.CASCADE)
	def __str__(self):
		return "message "+str(self.id)
	def fid(self):
		return str(id)