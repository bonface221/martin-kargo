from django.test import TestCase
from .models import *

# Create your tests here.

class ImageTest(TestCase):
  def setUp(self):
    self.user = Image(title='Race Car', description='very fast', landImage='.jpg', squareImage='.jpg', tallImage='.jpg')

  def test_instance(self):
    self.assertTrue(isinstance(self.user, Image))

  def test_save(self):
    self.user.save
    users = Image.objects.all()
    self.assertTrue(len(users) >0)

  def test_delete(self):
    self.user.save()
    self.user.delete()
    users = Image.objects.all()
    self.assertTrue(len(users)==0)
