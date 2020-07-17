from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blog(models.Model):

  CATEGORIES = [
    ('dmarketing', 'Digital Marketing'),
    ('wdesign', 'Web Development & Design'),
    ('msolutions', 'Marketing Solutions'),
    ('ranalytics', 'Research & Analytics'),
  ]

  title= models.CharField(max_length= 256)
  desc= models.CharField(max_length= 1024)
  author= models.CharField(max_length= 128)
  cover_img= models.ImageField(upload_to= 'acpl/img/')
  content= RichTextUploadingField(default= '')
  date= models.DateField()
  refr= models.CharField(max_length= 512, blank= True)
  categories= models.CharField(max_length= 128, choices= CATEGORIES, default= 'Digital Marketing')
  url= models.URLField(blank= True)

  def __str__(self):
    return self.title