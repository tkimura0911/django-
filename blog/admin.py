from django.contrib import admin
from .models import Post

# Register your models here.

#Adminページで見えるようにするため。作成したモデルを登録
admin.site.register(Post)
