from django.test import TestCase


class GraceLeeTest(TestCase):
	# this should set up the pseudo DB
	def setUp(self):
		UploadFile.objects.create(image="photo.jpg", comment="first photo")
		UploadFile.objects.create(image="picture.jpg", comment="second photo")
		UploadFile.objects.create(image="image.jpg", comment="third photo")

	def test_image_db(self):
		first = UploadFile.objects.get("photo.jpg")
		second = UploadFile.objects.get("picture.jpg")
		third = UploadFile.objects.get("image.jpg")
		
		self.assertEqual(first.img_comment(), 'first img')
		self.assertEqual(second.img_comment(), 'second img')
		self.assertEqual(third.img_comment(), 'third img')

	# tears the test down
	def tearDown(self):
		self.fixture


	# checks to see if imagelist returns any data
	def test_image_info(self):
		check_imagelist = imagelist[::]
		self.assertIsNotNone(imagelist)

	# checks if image is stored and resized
	def test_image_resize(self):
		# is the images url split?
		# cropped url set up properly?

		# test static serve request
		# recieves original image
		# stores original image
		# recieves new size
		# stores new size
		# returns new image

	def test_image_crop(self):
		# test static serve request
		# test is images exist in the DOCUMENT_ROOT
		# test if new image is cropped
		# test if cropped image is saved
		# test is image is returned


if __name__ == '__main__':
	unittest.main()














