from django.db import models

# Create your models here.
class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    rent = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    area =models.CharField(max_length=50)
    beds = models.CharField(max_length=50)
    baths = models.CharField(max_length=50)
    garage = models.CharField(max_length=50)

    def __str__(self):
        return self.title

