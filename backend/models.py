from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related
from rest_framework.fields import CurrentUserDefault
from rest_framework.permissions import IsAuthenticated

# Create your models here.


def upload_to(instance, filename):
    return 'paper/{filename}'.format(filename=filename)

def note_upload(instance, filename):
    return 'note/{title}'.format(filename=filename)

class Project(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(User, related_name="project",default=None,blank = True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Paper(models.Model):
    file_Name = models.CharField(max_length = 100)
    paper = models.FileField(blank=True,upload_to = upload_to, null=True)
    owner = models.ForeignKey(User, related_name='paper',default=None,blank = True, on_delete=models.CASCADE)
    
    project = models.ForeignKey(Project, related_name="paper", default=None, null=True, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Note(models.Model):
    title = models.CharField(max_length=20)
    note = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, related_name='note',default=None,blank = True, on_delete=models.CASCADE)
    related_to = models.ForeignKey(Paper, related_name = "note", null=True,default=None, on_delete=models.SET_NULL)  
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)




    