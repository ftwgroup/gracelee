from django.db import models
from urllib2 import urlopen
from django import forms


class UploadFile(models.Model):
	comment = models.CharField(max_length=255)
	image = models.FileField(upload_to='images')

	def __unicode__(self):
		return self.image.name + ' comment: (' + self.comment + ')'



