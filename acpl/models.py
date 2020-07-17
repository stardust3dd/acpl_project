from django.db import models

# Create your models here.
# class Blogs(models.Model):
#   title= models.CharField(max_length= 256)
#   desc= models.CharField(max_length= 1024, blank= True)
#   author= models.CharField(max_length= 128)
#   text= models.TextField(default= '')
#   img= models.ImageField(upload_to= 'acpl/img/')
#   refr= models.CharField(max_length= 512, blank= True)
#   categories= models.CharField(max_length= 128, default= '')
#   url= models.URLField(blank= True)

# class Cases(models.Model):
#   title= models.CharField(max_length= 256)
#   desc= models.CharField(max_length= 1024)
#   img= models.ImageField(upload_to= 'acpl/img/')
#   refr= models.CharField(max_length= 512, blank= True)
#   categories= models.CharField(max_length= 128)
#   url= models.URLField(blank= True)
#   pfile= models.FileField(upload_to= 'acpl/files/')

# class Teams(models.Model):
#   name= models.CharField(max_length= 256)
#   desg= models.CharField(max_length= 64)
#   pic= models.ImageField(upload_to= 'acpl/img')
#   linkd= models.URLField(blank= True)