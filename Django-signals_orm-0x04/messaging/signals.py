
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory
from django.contrib.auth.models import User

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.receiver,
            message=instance
        )

@receiver(post_delete, sender=User)
def delete_user_related_data(sender, instance, **kwargs):
        Message.objects.filter(sender=instance).delete()
        Message.objects.filter(receiver=instance).delete()
        Notification.objects.filter(user=instance).delete()
        MessageHistory.objects.filter(edited_by=instance).delete()

@receiver(pre_save, sender=Message)
def log_message_edits(sender, instance, **kwargs):
    if instance.id:
        try:
            original = Message.objects.get(id=instance.id)
            if original.content != instance.content:
                MessageHistory.objects.create(
                    message=original,
                    old_content=original.content,
                    edited_by=getattr(instance, '_edited_by', None)
                )
                instance.edited = True
        except Message.DoesNotExist:
            pass
