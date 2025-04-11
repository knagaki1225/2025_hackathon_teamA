from django.contrib import admin
from .models import Department, Review, Category, Class, Reply, Good

admin.site.register(Category)
admin.site.register(Class)
admin.site.register(Reply)
admin.site.register(Good)
admin.site.register(Department)
admin.site.register(Review)

# Register your models here.
