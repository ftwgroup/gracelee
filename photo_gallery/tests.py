from django.test import TestCase
from django.test.client import Client
from photo_gallery.models import UploadFile
from photo_gallery.views import image_resize, image_crop, domain_path, parse_url, ensure_dir, image_info
from django.http import Http404
import re


class GraceLeeTest(TestCase):
	# this should set up the pseudo DB
	def setUp(self):
		UploadFile.objects.create(image="photo.jpg", comment="first photo")
		UploadFile.objects.create(image="picture.jpg", comment="second photo")
		UploadFile.objects.create(image="image.jpg", comment="third photo")
		#
	def test_parse_url(self):
		url = 'http://businessnetworking.com/uploads/2012/happy-face.jpg'
		pattern = re.compile(r'^http://([^/\r\n]+)/([^\r\n]*)$')
		matcher = pattern.match(url)
		domain_name = matcher.group(1)
		self.assertRegexpMatches(url, pattern)
		self.assertTrue(matcher.group(1) == 'businessnetworking.com')
		self.assertTrue(matcher.group(2) == '/uploads/2012/happy-face.jpg')
		# in a specific format?
		#
	def test_domain_path(self):
		# is the correct format being concatenated?
		pass

	def test_get_image(self):
		remote_url = 'http://fredtopeka.files.wordpress.com/2012/10/693952main_pia15817-full_full.jpg'
		local_url = 'http://50X50/businessnetworking.com/wp-content/uploads/2012/04/happy-face.jpg/'
		false_url = 'http://20x20/falseurl.net/fakepicture.jpg'
		
		pass

	def test_ensure_dir(self):
		pass
		
	def test_image_resize(self):
		pass
		
	def test_image_crop(self):
		pass








