from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Product(models.Model):
	title = models.CharField(default='美好生活', max_length=50)
	intro = models.TextField(default='美好生活开始')
	url   = models.CharField(default='http://', max_length=100)
	icon  = models.ImageField(default='2345_image_file_copy_1.jpg',upload_to = 'image/')
	image = models.ImageField(default='吉祥物02.jpg',upload_to='image/')
	
	votes = models.IntegerField(default=1)
	pub_date = models.DateTimeField()
	hunter  = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def text(self):
		return self.intro[:150] + '...'
