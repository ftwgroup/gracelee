"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


####################
# sudo testing code:


class GraceLeeTest(TestCase):
	#checks to see if imagelist returns any data
	def test_image_info(self):
		check_imagelist = imagelist[::]
		self.assertIsNotNone(imagelist)

	# checks if image:
	# stores original, stores new size
	def test_image_resize(self):


if __name__ == '__main__':
	unittest.main()














