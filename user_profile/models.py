from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractUser


class User(AbstractBaseUser):


    username = models.CharField('username', max_length=10, unique=True, db_index=True)
    email = models.EmailField('email address', unique=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    #REQUIRED_FIELDS = ['email',]

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return  self.username

    def __unicode__(self):
        return self.username


class TestUser():
    title = models.CharField('title', max_length=100, unique=False)





