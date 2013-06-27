from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
from django.forms import ModelForm
from django.conf import settings
from django.views import static
from django.db import models
from django.contrib.sites.models import Site
from models import UploadFile
from forms import ImageForm
import json
import re # regex
import os
from wand.image import Image
from urllib2 import urlopen
from StringIO import StringIO
import requests


DOCUMENT_ROOT = settings.MEDIA_ROOT

def parse_url(url):
	pattern = re.compile(r'^http://([^/\r\n]+)/([^\r\n]*)$')
	matcher = pattern.match(url)
	domain_name = matcher.group(1)
	path_name = matcher.group(2)
	return domain_name, path_name

def domain_path(orig_url, height, width, filetype):
	return '%s-%sx%s.%s' % (orig_url, height, width, filetype)


def ensure_dir(path):
	path_directory = os.path.abspath(os.path.dirname(path))
	#print path
	#print path_directory
	if not os.path.exists(path_directory):
		os.makedirs(path_directory)
	return path

def image_resize(request, height, width, url):
	domain_name, path_name = parse_url(url)
	orig_url, filetype = path_name.rsplit('.', 1)
		# 'photo', '.jpg'
	resized_url = domain_path(orig_url, height, width, filetype)
		# photo-50x50.jpg
	try:
		return static.serve(request,domain_name+'/'+resized_url, document_root=DOCUMENT_ROOT)
	except Http404:
		filename = get_image()
			with Image(filename=ensure_dir(filename) as img:
				with img.clone() as i:
					i.resize(int(width), int(height))
					i.save(filename=ensure_dir(os.path.join(DOCUMENT_ROOT, domain_name, resized_url)))
		return static.serve(request, domain_name+'/'+resized_url, document_root=DOCUMENT_ROOT)

def get_image(domain_name, path_name):
	filename = os.path.join(DOCUMENT_ROOT, domain_name, path_name)
	if os.path.exists(filename):
		return filename
	else:
		site = Site.objects.get(id=settings.SITE_ID)
		if domain_name == site.domain:
			return os.path.join(DOCUMENT_ROOT, path_name)
		else:
			try:
				url = 'http://'+domain_name+'/'+path_name
				remote_file = requests.get(url)
				with Image(file=StringIO(remote_file.content)) as img:
					img.save(filename=ensure_dir(filename))
			except Exception, e:
				print e
			finally:
				remote_file.close()
				return filename

def resize():
	i.resize(int(width), int(height))
	i.save(filename=ensure_dir(os.path.join(DOCUMENT_ROOT, domain_name, resized_url)))

def image_crop(request, left, top, right, bottom, url):
	orig_url, filetype = url.rsplit('.', 1)
		# 'photo', '.jpg'
	cropped_url = domain_path(orig_url, left, top, right, bottom, filetype)
		# photo-50x50-50x50.jpg
	try:
		return static.serve(request, cropped_url, document_root=DOCUMENT_ROOT)
	except Http404:
		with Image(filename=os.path.join(DOCUMENT_ROOT, url)) as img:
			img.crop(int(left), int(top), int(right), int(bottom))
			img.save(filename=ensure_dir(os.path.join(DOCUMENT_ROOT, cropped_url)))
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









