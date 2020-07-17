from django.db import models

# Create your models here.
class Member(models.Model):
  name= models.CharField(max_length= 256)
  desg= models.CharField(max_length= 64)
  pic= models.ImageField(upload_to= 'acpl/img')
  linkd= models.URLField(blank= True)

  def __str__(self):
    return self.name