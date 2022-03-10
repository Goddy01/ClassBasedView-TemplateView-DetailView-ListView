from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    '''Creates fields for the School Model and returns the school.name.'''
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        '''Returns the details of a specific school.'''
        return reverse("basic_app:school_detail", kwargs={'pk':self.pk})

class Student(models.Model):
    '''Creates fields for the Student Model and returns student.name.'''
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE) # Creates a many to one relationship between the School model and the school attribute in the Student Model.

    def __str__(self):
        return self.name