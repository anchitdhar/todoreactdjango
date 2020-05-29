from django.db import models

class Todo(models.Model):
	title= models.CharField(max_length=10)
	description = models.TextField(max_length=30)

	def __str__(self):
		return self.title
