from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.

# Adding some fields to make admin panel look good now make a field named tags inside the post and add value TAGS the tupple that have the data for tags

TAGS = (('TECH', 'TECH'), ('JOBS', 'JOBS'), ('Django','Django'), ('React','React'))

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = HTMLField()
    dated = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
    # Active = models.BooleanField(default=True)
    is_deleted =models.BooleanField(default=False)
    # For created at filter 
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)
    # Add a filter to see it the post have this value or not
    sub_title = models.CharField(max_length=100, blank=True, null=True) 
    #  Pass tags value here
    tags = models.CharField(choices=TAGS, max_length=100, default='TECH')
    
    def __str__(self):
        return self.title