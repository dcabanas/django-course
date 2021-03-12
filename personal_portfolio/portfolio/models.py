from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio')
    url = models.URLField(blank=True)

    # useful for display in the admin page
    def __str__(self):
        return self.title