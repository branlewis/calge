from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings
import datetime
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _


class BaseProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                primary_key=True)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField('Profile picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    bio = models.CharField("Short Bio", max_length=200, blank=True, null=True)
    email_verified = models.BooleanField("Email verified", default=False)
    # Add extra profile details
    address = models.CharField("Address", max_length=100, blank=True, null=True)
    school = models.CharField("School", max_length=80, blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    foodAllergy = models.CharField("Food Allergies", max_length=200, blank=True, null=True)
    specialNeeds = models.CharField("Special Needs", max_length=200, blank=True, null=True)
    dob = models.DateField(_("Date"), default=datetime.date.today)
    parent = models.CharField("Parent/Guardian's Name", max_length=40,
                                blank=True, null=True)
    parentPhone = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Profile(BaseProfile):
    def __str__(self):
        return "{}'s profile". format(self.user)
