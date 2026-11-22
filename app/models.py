from django.db import models
class Profile(models.Model):
    name=models.CharField(max_length=225)
    image=models.ImageField(upload_to='profiles/', blank=True, null=True)
    about=models.TextField()
    email=models.EmailField(unique=True)
    skills=models.TextField()    