from django.db import models
from social_media.common.models import BaseModel
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager as BUM
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator


class BaseUserManager(BUM):
    def create_user(self, username, email, is_active=True, is_admin=False, password=None):
        if not username:
            raise ValueError("Users must have an username ")

        user = self.model(username=username, email= email, is_active=is_active, is_admin=is_admin)

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, username,email:str, password=None):
        user = self.create_user(
            username=username,
            is_active=True,
            is_admin=True,
            password=password,
            email=email,
        )

        user.is_superuser = True
        user.save(using=self._db)

        return user


class BaseUser(BaseModel, AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
                            verbose_name = "email address" ,
                            unique       =  True ,
                            blank        = True , 
                            )
    
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
                            _("username"),
                            max_length = 40,
                            unique=True ,
                            help_text=_(
                                "Required. 40 characters or fewer. Letters, digits and @/./+/-/_ only."
                            ),
                            validators=[username_validator],
                            error_messages={
                                "unique": _("A user with that username already exists."),
                            },
                            )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = BaseUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    def __str__(self):
        return self.email

    def is_staff(self):
        return self.is_admin









