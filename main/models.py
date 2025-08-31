from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(verbose_name="Project Name")
    description = models.TextField()
    # location = models.

    def __str__(self):
        return self.name
    