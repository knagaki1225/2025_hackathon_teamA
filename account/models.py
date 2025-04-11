# account/models.py
import os,uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

#アップロードされたファイルをUUIDを使用して一意の名前に変換する関数
def icon_upload_function(instance, filename):
    ext = os.path.splitext(filename)[1] #ファイル名から拡張子を取り出す
    filename = f"{uuid.uuid4()}.{ext}" #UUID＋拡張子に変更
    return os.path.join('profile_icons', filename) #変更後のファイル名を返す

class User(AbstractUser):
    department_id = models.ForeignKey("review.Department", on_delete=models.CASCADE, default=2)
    grade = models.IntegerField(default=1)
    icon_url = models.ImageField(upload_to=icon_upload_function, default='profile_icons/default.jpg')
    language = models.CharField(max_length=20, null=True, blank=True)
    career = models.CharField(max_length=20, null=True, blank=True)
    my_ditail = models.TextField(null=True, blank=True)
    admin_flg = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    del_flg = models.BooleanField(default=False)
