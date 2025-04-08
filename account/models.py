# account/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    department_id = models.ForeignKey("review.Department", on_delete=models.CASCADE)
    grade = models.IntegerField(default=1)
    icon_url = models.TextField(default='default.jpg')
    language = models.CharField(max_length=20, null=True, blank=True)
    career = models.CharField(max_length=20, null=True, blank=True)
    my_ditail = models.TextField(null=True, blank=True)
    admin_flg = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    del_flg = models.BooleanField(default=False)

