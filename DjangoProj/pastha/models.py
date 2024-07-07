from django.db import models
from django.utils import timezone


# Create your models here.
class PasthaVarity(models.Model):
    PASTHA_TYPE_CHOICES = [
        ('ch','chilly'),
        ('sl','salty'),
        ('sp','spicy'),
        ('nr','normal'),
    ]
    name = models.CharField(max_length=255)
    # An error related to image field is generated named as pillow
    image = models.ImageField(upload_to='astha/')
    date_add =models.DateTimeField(default=timezone.now)

    type = models.CharField(max_length=2,choices=PASTHA_TYPE_CHOICES)

    def __str__(self):
        return self.name