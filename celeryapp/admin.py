from django.contrib import admin
from celeryapp.models import Post, Category

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
