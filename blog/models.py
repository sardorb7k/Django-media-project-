from django.db import models

# Create your models here.

class Photos(models.Model):
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="photos")

    def __str__(self) -> str:
        return self.photo