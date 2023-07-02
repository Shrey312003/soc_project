from django.db import models

# Create your models here.

class Courses(models.Model):
    courseCode = models.CharField(max_length=5,default=None)
    courseId = models.CharField(max_length=5,default = None,primary_key=True)

    def __str__(self):
        return self.courseCode

class Admin_info(models.Model):
    Username = models.CharField(max_length=100,default='',primary_key=True)
    Password = models.CharField(max_length=50,default='')

    def __str__(self):
        return self.Username
    
class Ta_info(models.Model):
    Roll = models.CharField(max_length=100,default='',primary_key=True)
    Password = models.CharField(max_length=50,default='')
    is_logged = models.BooleanField(default=False)
    course = models.ForeignKey(Courses,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.Roll

class Student_info(models.Model):
    Roll = models.CharField(max_length=100,default='',primary_key=True)
    Password = models.CharField(max_length=50,default='')
    is_logged = models.BooleanField(default=False)
    course = models.ForeignKey(Courses,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.Roll
