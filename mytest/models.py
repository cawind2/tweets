from django.db import models
from user_profile.models import User


class Tweet(models.Model):
    """
    Tweet model
    """

    user = models.ForeignKey(User, null=True)
    text = models.CharField(max_length=160)
    created_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)


