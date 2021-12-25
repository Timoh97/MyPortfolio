
from django.db import models

# Create your models here.

from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Project(models.Model):
  image = CloudinaryField('image')
  project_name = models.TextField(max_length=30)
  description = models.TextField()
  significance = models.TextField()
  category = models.TextField()
  url = models.URLField(blank=True)
  future_improvements= models.TextField()
  date_posted = models.DateTimeField(auto_now=True)
  
  
  
  # Save image method
  def save_project(self):
    self.save()
    
  # Get all images method
  @classmethod
  def get_project_by_id(cls, id):
        project = cls.objects.get(id=id)
        return project

  @classmethod
  def get_all_projects(cls):
        projects = cls.objects.all()
        return projects

  @classmethod
  def get_all_projects_by_user(cls, user):
        projects = cls.objects.filter(user=user)
        return projects
      
  @classmethod
  def search_image(cls,search_term):
       images = cls.objects.filter(category__icontains=search_term)
       return images

  # @classmethod
  # def search_image(cls,search):
  #       image = cls.objects.filter(name__icontains=search)
  #       return image
  
def __str__(self):
      return self.name