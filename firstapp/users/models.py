from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.

# todo define
# class AnotherPermissionsMixin(models.Model):
#     """
#     Add the fields and methods necessary to support the Group and Permission
#     models using the ModelBackend.
#     """
#     is_superuser = models.BooleanField(
#         _('superuser status'),
#         default=False,
#         help_text=_(
#             'Designates that this user has all permissions without '
#             'explicitly assigning them.'
#         ),
#     )
#     groups = models.ManyToManyField(
#         AnotherGroup,
#         verbose_name=_('groups'),
#         blank=True,
#         help_text=_(
#             'The groups this user belongs to. A user will get all permissions '
#             'granted to each of their groups.'
#         ),
#         related_name="user_set",
#         related_query_name="user",
#     )
#     user_permissions = models.ManyToManyField(
#         AnotherPermission,
#         verbose_name=_('user permissions'),
#         blank=True,
#         help_text=_('Specific permissions for this user.'),
#         related_name="user_set",
#         related_query_name="user",
#     )
#
#     class Meta:
#         abstract = True
#
#
# class AnotherGroup(models.Model):
#     # Groupモデルの内容をコピペ、Metaに以下追加
#     class Meta:
#         db_table = "hoge"
#
#
# class AnotherPermission(models.Model):
#     # Permissionモデルの内容をコピペ、Metaに以下追加
#     class Meta:
#         db_table = "hoge"

# todo: add users image field
class User(AbstractBaseUser, AnotherPermissionsMixin):
    email = models.EmailField('メールアドレス', blank=True)
    username = models.CharField(
        'ニックネーム', blank=False, max_length=20, help_text='20文字以内で入力してください。', unique=True,
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Designates whether the user can log into this admin site.',
    )
    is_active = models.BooleanField(
        'active',
        default=True,
        help_text='Designates whether this user should be treated as active. '
                  'Unselect this instead of deleting accounts.',
    )
