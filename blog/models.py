from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	#各プロパティにmodels関数が用意している型を定義する（型で初期化ってことかな）
	#他のモデルへのリンク
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	#２００文字までのテキストフィールド
	title = models.CharField(max_length=200)
	#制限なしのテキストフィールド
	text = models.TextField()
	#日付と時間のフィールド
	created_date = models.DateTimeField(
			default=timezone.now)
	#日付と時間のフィールド
	published_date = models.DateTimeField(
			blank=True, null=True)
			
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	
	def __str__(self):
		return self.title
