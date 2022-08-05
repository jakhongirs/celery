from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
from celeryapp.tasks import update_count

from celeryapp.models import Post


@receiver(post_save, sender=Post)
def add_count(sender, instance, created, **kwargs):
    if created:
        update_count.delay(instance.category.id)


@receiver(pre_delete, sender=Post)
def delete_count(sender, instance, **kwargs):
    update_count.delay(instance.category.id)
