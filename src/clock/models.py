from django.db import models
from django.conf import settings
import uuid
# import requests


# Create your models here.

class shiftTime(models.Model):
    #user = request.user
    #id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #user = models.OneToOneField(settings.AUTH_USER_MODEL,
    #                            on_delete=models.CASCADE,
    #                            primary_key=False)
    #slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    timeIn = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    timeOut = models.TimeField(auto_now=False, auto_now_add=False, null=True)

    def __unicode__(self):
        return '%s' % self.title
