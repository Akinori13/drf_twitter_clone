import uuid

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_data):
        user = self.model(
            email=self.normalize_email(email),
            **extra_data,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_data):
        extra_data.setdefault("is_staff", True)
        extra_data.setdefault("is_staff", True)
        extra_data.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_data)


class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(
        verbose_name="ID",
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )
    username = models.CharField(
        verbose_name="名前",
        max_length=50,
        unique=True,
    )
    email = models.EmailField(verbose_name="Email", max_length=50, unique=True)
    joined_at = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username
