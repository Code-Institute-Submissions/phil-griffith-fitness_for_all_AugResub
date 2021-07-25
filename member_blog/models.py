from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MemberBlog(models.Model):
    """
    A blog model for capturing member blogs
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                                     null=True, blank=True, related_name='user')   
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    comment = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title
