from django.db import models

# Create your models here.
class Student(models.Model):
    objects = None
    image = models.ImageField(upload_to='student_images/', null=True, blank=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    admission =models.IntegerField()
    gender = models.CharField(max_length=20)
    course = models.CharField(max_length=20)

    # constructor that returns our class variables
    def __str__(self):
        return self.name

class Course(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    description = models.TextField()
    credits = models.IntegerField()
   
