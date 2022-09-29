from django.db import models
from django.utils import timezone

class Leads(models.Model):
    #enumaration for status fields
    class Status(models.TextChoices):
        SUBSCRIPBED = 'SUB', 'Subscribed'
        UNSUBSCRIBED = 'UNS', 'unsubscribed'

    email_id = models.EmailField(max_length=254)
    action_time = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length= 3,
        choices= Status.choices,
        default='SUB'
    )

    class Meta:
        ordering = ['-action_time']
        indexes = [
            models.Index(fields=['-action_time'])
        ]

    def __str__(self):
        return self.email_id
