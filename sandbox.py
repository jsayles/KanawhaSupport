import os

from django.conf import settings
from django.utils.timezone import localtime, now
from django.contrib.auth.models import User


from portal.models import *


user = User.objects.first()
