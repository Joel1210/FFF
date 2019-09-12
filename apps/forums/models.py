from __future__ import unicode_literals
from django.db import models
from ..user.models import User

class ContentManager(models.Manager):
    def comment_validator(self, postData):
        errors = {}
        if len(postData['comment']) > 1000:
            errors['comment'] = 'Please keep messages under 1000 characters'
        if len(postData['comment']) == 0:
            errors['comment'] = "Can't submit a blank comment"
        return errors
    def reply_validator(self, postData):
        errors = {}
        if len(postData['reply']) > 1000:
            errors['reply'] = 'Please keep replies under 1000 characters'
        return errors
class Comment(models.Model):
    content = models.CharField(max_length= 1000)
    commenter = models.ForeignKey(User, related_name= "comments")
    eventId = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ContentManager()

class Reply(models.Model):
    content = models.CharField(max_length=1000)
    Replier = models.ForeignKey(Comment, related_name="replies")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ContentManager()