from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.

# todo: create this class later
# class BaseTimestampModel(object):
#     pass


class User(AbstractBaseUser, PermissionsMixin):
    pass
