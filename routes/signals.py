from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AirportRoute


@receiver(post_save, sender=AirportRoute)
def auto_position_and_link(sender, instance, created, **kwargs):
    if created:
        last = AirportRoute.objects.exclude(id=instance.id).order_by("-position").first()
        instance.position = last.position + 1 if last else 1
        instance.save()
        if last:
            last.next_node = instance
            last.save()
