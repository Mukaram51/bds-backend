from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(verbose_name="Project Name")
    description = models.TextField()
    is_completed = models.BooleanField(verbose_name='Work Progress', default=False)
    # images = models.ImageField()
    # location = models.TextField()

    def __str__(self):
        return self.name
    