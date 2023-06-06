from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # generic relation
    # Identifying the type of an object the user likes
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # Referencing that particular object
    object_id = models.PositiveIntegerField()
    # reading an actual object
    content_object = GenericForeignKey()
