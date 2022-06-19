from django.db import models

# Create your models here.
class Blog(models.Model):
    mainHeading = models.CharField(max_length=200)
    mainImage = models.FileField(upload_to="Image")
    qoutes = models.TextField()
    qoutes_author = models.CharField(max_length=100)
    content = models.TextField()        
    date = models.DateField()