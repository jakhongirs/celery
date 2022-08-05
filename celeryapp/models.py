from django.db import models
from helpers.models import BaseModel


# Create your models here.


class Category(BaseModel):
    title = models.CharField(max_length=128)
    post_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Post(BaseModel):
    title = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title
