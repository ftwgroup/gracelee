from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
from django.forms import ModelForm
from forms import ImageForm
from models import UploadFile
from django.db import models
import json
import re # import regex
import os
from django.conf import settings
from django.views import static

from wand.image import Image
from urllib2 import urlopen


DOCUMENT_ROOT = settings.MEDIA_ROOT

def image_resize(request, height, width, url):
	orig_url, filetype = url.rsplit('.', 1)
	resized_url = '%s-%sx%s.%s' % (orig_url, height, width, filetype)
		#photo-50x50.jpg
	try:
		return static.serve(request, resized_url, document_root=DOCUMENT_ROOT)
	except Http404:

		with Image(filename=os.path.join(DOCUMENT_ROOT, url)) as img:
			with img.clone() as i:
				i.resize(int(width), int(height))
				i.save(filename=os.path.join(DOCUMENT_ROOT, resized_url))
		return static.serve(request, resized_url, document_root=DOCUMENT_ROOT)

def image_crop(request, left, top, right, bottom, url):
	orig_url, filetype = url.rsplit('.', 1)
	cropped_url = '%s-%sx%s-%sx%s.%s' % (orig_url, left, top, right, bottom, filetype)
		# photo-50x50-50x50.jpg
	try:
		return static.serve(request, cropped_url, document_root=DOCUMENT_ROOT)
	except Http404:
		with Image(filename=os.path.join(DOCUMENT_ROOT, url)) as img:
			img.crop(int(left), int(top), int(right), int(bottom))
			img.save(filename=os.path.join(DOCUMENT_ROOT, cropped_url))
		return static.serve(request, cropped_url, document_root=DOCUMENT_ROOT)

def image_info(request):
	imagelist = []
	for image in UploadFile.objects.all():
		image_dict = {
		'Image: ': image.image.url,
		'Comment: ': image.comment,
		}
		imagelist.append(image_dict)
	return HttpResponse(json.dumps(imagelist))









