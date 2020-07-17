from django.db import models

# Create your models here.
class Case(models.Model):

  VERTICALS = [
    ('dmarketing', 'Digital Marketing'),
    ('msolutions', 'Marketing Solutions'),
    ('ranalytics', 'Research & Analytics'),
  ]

  title= models.CharField(max_length= 256)
  desc= models.CharField(max_length= 1024)
  img= models.ImageField(upload_to= 'acpl/img/')
  categories= models.CharField(max_length= 128, choices= VERTICALS, default= 'Digital Marketing')
  url= models.URLField(blank= True)
  pfile= models.FileField(upload_to= 'acpl/files/')

  def __str__(self):
    return self.title