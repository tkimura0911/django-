from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	#�e�v���p�e�B��models�֐����p�ӂ��Ă���^���`����i�^�ŏ��������Ă��Ƃ��ȁj
	#���̃��f���ւ̃����N
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	#�Q�O�O�����܂ł̃e�L�X�g�t�B�[���h
	title = models.CharField(max_length=200)
	#�����Ȃ��̃e�L�X�g�t�B�[���h
	text = models.TextField()
	#���t�Ǝ��Ԃ̃t�B�[���h
	created_date = models.DateTimeField(
			default=timezone.now)
	#���t�Ǝ��Ԃ̃t�B�[���h
	published_date = models.DateTimeField(
			blank=True, null=True)
			
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	
	def __str__(self):
		return self.title
