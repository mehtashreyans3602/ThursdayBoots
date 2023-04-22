from django.db import models

class Shoe(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unisex'),
    )
    model_name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=100)
    style = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.ImageField(upload_to='shoe_photos/')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U')

    def __str__(self):
        return self.model_name + ' - ' + self.color
