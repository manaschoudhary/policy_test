from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse
# Create your models here.


class phase_1(models.Model):

        problem_images = models.IntegerField(help_text="Number of images of existing problems",blank=True,null=True)
        problem_images_upload = models.ImageField(upload_to = 'images',blank=True,null=True)
 
	    
        
        

      
 
