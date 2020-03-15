import logging
import random, string

from django.db import models
from django.conf import settings
from django.utils.timezone import localtime, now
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


logger = logging.getLogger(__name__)


################################################################################
# User Models
################################################################################


def user_photo_path(instance, filename):
    file_ext = filename.split('.')[-1].lower()
    return "user_photos/%s.%s" % (instance.user.username, file_ext)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=False, related_name="profile", on_delete=models.CASCADE)
    phone = models.CharField(max_length=16, blank=True)
    photo = models.ImageField(upload_to=user_photo_path, blank=True, null=True)
    valid_billing = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "Profile: " + self.user.get_full_name()

    class Meta:
        ordering = ['user__first_name', 'user__last_name']
        get_latest_by = "last_modified"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def user_save_callback(sender, **kwargs):
    user = kwargs['instance']
    if not UserProfile.objects.filter(user=user).count() > 0:
        UserProfile.objects.create(user=user)


################################################################################
# Space Models
################################################################################


def space_logo_path(instance, filename):
    file_ext = filename.split('.')[-1].lower()
    return "space_logos/%s.%s" % (instance.code, file_ext)


class Space(models.Model):
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=32, unique=True)
    address1 = models.CharField(max_length=128, blank=True)
    address2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=128, blank=True)
    state = models.CharField(max_length=2, blank=True)
    postcode = models.CharField(max_length=16, blank=True)
    country = models.CharField(max_length=128, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    admin_email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=16, blank=True)
    website = models.URLField()
    logo = models.ImageField(upload_to=space_logo_path, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


@receiver(pre_save, sender=Space)
def space_save_callback(sender, **kwargs):
    space = kwargs['instance']
    new_code = ''
    while new_code == '' or Space.objects.filter(code=new_code).count() > 0:
        new_code = 'SP' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    space.code = new_code
