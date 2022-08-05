from core.celery import app
from .models import Category, Post


@app.task()
def update_count(id):
    category = Category.objects.get(pk=id)

    category.post_count = Post.objects.filter(category=category).count()
    category.save()
