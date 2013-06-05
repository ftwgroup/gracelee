from django.forms import ModelForm
from models import UploadFile
from django.db import models
from django import forms

class ImageForm(ModelForm):
	class Meta:
		model = UploadFile
		fields = ('image', 'comment')

ImageForm()


