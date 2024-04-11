from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

@receiver(post_save, sender=get_user_model())
def assign_to_group(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='clientes')
        instance.groups.add(group)
