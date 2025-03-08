from django.db import models
from PIL import Image
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.
class Course(models.Model):
    """ create the course model"""
    FORMAT_CHOICES = [
    ('slide', 'Slide-based'),
    ('text', 'Text-based'),
]
    
    
    format = models.CharField(max_length=10, choices = FORMAT_CHOICES, default='text')
    title = models.CharField(max_length=200 , default ='')
    content = CKEditor5Field('content', config_name= 'extends')
    #slides = models.JSONField(blank = True, null=True, default= dict) 
    file = models.FileField(upload_to='files/',default='files/default_file.pdf')
    image = models.ImageField(upload_to='images/', blank=True, null=True, default='images/default_image.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   # featured = models.BooleanField(default = False)


    def __str__(self):
        """"string representation of the model"""
        return self.title

 