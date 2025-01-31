from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.dispatch import receiver

@receiver(post_save, sender=User)
def add_user_to_default_group(sender, instance, created, **kwargs):
    if created:
        default_group, _ = Group.objects.get_or_create(name='User')
        instance.groups.add(default_group)