from django.db import models
CHOICES_PRODUCTS=(
    ['SMARTPHONES','Smartphones'],
    ['CHARGERS','Chargers'],
    ['BACK COVER','Backcover']
)
class Profile(models.Model):
    name=models.CharField(max_length=225)
    image=models.ImageField(upload_to='profiles/', blank=True, null=True)
    about=models.TextField()
    email=models.EmailField(unique=True)
    skills=models.TextField()    
class Product(models.Model):
    product_name=models.CharField(max_length=225)
    product_description=models.TextField()
    category=models.CharField(max_length=225,choices=CHOICES_PRODUCTS)