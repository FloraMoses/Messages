from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Super User
# username: flora
# password: class123

class Category(models.Model):
    user = models.ForeignKey(User)
    category_name = models.CharField(max_length=25)

class Message(models.Model):
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    msg_text = models.CharField(max_length=300)

class Reply(models.Model):
    user = models.ForeignKey(User)
    msg = models.ForeignKey(Message)
    reply_text = models.CharField(max_length=300)
