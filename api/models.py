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
    Name = models.CharField(max_length=100,default='')
    Roll = models.CharField(max_length=100,default='',primary_key=True)
    Password = models.CharField(max_length=50,default='')
    is_logged = models.BooleanField(default=False)
    course = models.ManyToManyField(Courses,null=True)

    def __str__(self):
        return self.Roll

class Student_info(models.Model):
    Name = models.CharField(max_length=100,default='')
    Roll = models.CharField(max_length=100,default='',primary_key=True)
    Password = models.CharField(max_length=50,default='')
    is_logged = models.BooleanField(default=False)
    course = models.ManyToManyField(Courses,null=True)

    def __str__(self):
        return self.Roll

class Attendance_sessions(models.Model):
    CourseId = models.CharField(max_length=5,default='')
    Date = models.DateField(default='')
    Start = models.TimeField(default='')

    def __str__(self):
        return str(self.id) + " " +self.CourseId
    
class Attendance_Records(models.Model):
    Session = models.ForeignKey(Attendance_sessions,on_delete=models.CASCADE,default='')
    CourseId = models.CharField(max_length=5,default='')
    Roll = models.CharField(max_length=100, default='')
    Attend_time = models.TimeField(default='')

    def __str__(self):
        return self.Roll