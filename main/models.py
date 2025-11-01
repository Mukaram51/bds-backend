from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    name = models.CharField(verbose_name="Project Name")
    description = models.TextField()
    is_completed = models.BooleanField(verbose_name='Work Progress', default=False)
    images = models.ImageField(upload_to='media')
    # location = models.TextField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    