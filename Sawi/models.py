from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class CommonInfo(models.Model):
    firstname = models.CharField("Firstname",max_length = 20)
    lastname = models.CharField("Lastname", max_length = 20)
    sex = models.CharField("Sex", max_length = 15)
    DOB = models.DateField("Birth")
    
    class Meta:
        abstract = True;

#• username
#• password
#• email
#• first_name
#• last_name

class Course(models.Model):
    title = models.CharField(max_length = 300)
    description = models.CharField(max_length = 300)
    duration = models.CharField(max_length = 30)

class Student(models.Model):
    user = models.ForeignKey(User);
    course = models.ForeignKey(Course)
    address = models.CharField(max_length = 200);
    DOB = models.DateField()
    sex = models.CharField(max_length = 20)


class Classes(models.Model):
    course = models.ForeignKey(Course)
    time = models.DateTimeField()
    duration = models.CharField(max_length = 20)
    description = models.CharField(max_length = 100)

class Event(models.Model):
    name = models.CharField(max_length = 20)
    date = models.DateTimeField()
    description = models.CharField(max_length = 100)
    venue = models.CharField(max_length = 50)


class Gallery(models.Model):
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 200)
    event = models.ForeignKey(Event)
    date = models.DateTimeField()

class Management(models.Model):
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    position = models.CharField(max_length = 50)
    qualification = models.CharField(max_length = 50)
    image = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)

class Institution(models.Model):
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200);
    description = models.CharField(max_length = 200)
    about = models.TextField()
    date = models.DateTimeField()
    motto = models.CharField(max_length = 100)
    
class News(models.Model):
    title = models.CharField(max_length = 50);
    brief = models.CharField(max_length = 100);
    details = models.TextField();
    datePosted = models.DateTimeField();
    
    def recentNews(self):
        
        pass
       # return self.
    

    
