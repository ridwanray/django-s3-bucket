from django.db import models
from core.storage_backends import PrivateMediaStorage

class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    published = models.BooleanField(default=True)
    extra_info = models.CharField(max_length=50,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    file =  models.FileField(blank=True, null=True)
    private_file = models.FileField(storage=PrivateMediaStorage(), blank=True, null=True)



