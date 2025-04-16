from django.db import models

# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    del_flg = models.BooleanField(default=False)

    def __str__(self):
        return self.department_name

class Review(models.Model):
    user_id = models.ForeignKey("account.User", on_delete=models.CASCADE)
    class_id = models.ForeignKey("review.Class", on_delete=models.CASCADE)
    review_num = models.IntegerField(default=5)
    comment = models.TextField(null=True, blank=True)
    anonymity_flg = models.BooleanField(default=False) #匿名フラグ
    create_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    del_flg = models.BooleanField(default=False)

class Good(models.Model):
    user_id = models.ForeignKey("account.User", on_delete=models.CASCADE)
    review_id = models.ForeignKey("review.Review", on_delete=models.CASCADE, related_name='good')
    create_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    del_flg = models.BooleanField(default=False)

class Reply(models.Model):
    user_id = models.ForeignKey("account.User", on_delete=models.CASCADE)
    review_id = models.ForeignKey("review.Review", on_delete=models.CASCADE)
    reply = models.TextField(default='reply')
    anonymity_flg = models.BooleanField(default=False) #匿名フラグ
    create_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    del_flg = models.BooleanField(default=False)

class Class(models.Model):
    user_id = models.ForeignKey("account.User", on_delete=models.CASCADE)
    class_name = models.CharField(max_length=20)
    category_id = models.ForeignKey("review.Category", on_delete=models.CASCADE)
    difficulty = models.IntegerField(default=1)
    comment = models.TextField(null=True, blank=True)
    priority_idx = models.IntegerField(default=100)
    create_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    del_flg = models.BooleanField(default=False)

    def __str__(self):
        return self.class_name

class Category(models.Model):
    category_name = models.CharField(max_length=20)
    priority_idx = models.IntegerField(default=100)
    create_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    del_flg = models.BooleanField(default=False)

    def __str__(self):
        return self.category_name