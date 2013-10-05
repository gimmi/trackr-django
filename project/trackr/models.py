from django.db import models

class Tag(models.Model):
	name = models.CharField(max_length=100)

class Item(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	tags = models.ManyToManyField(Tag)
