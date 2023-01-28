from django.db import models
from django.db.models.aggregates import Max

# Create your models here.



class Student(models.Model):
    name = models.CharField(max_length=255, null = True, blank = True)
    contact = models.CharField(max_length = 12, unique=True)
    email = models.EmailField(null = True, blank = True)
    school_name = models.CharField(max_length=255, null = True, blank = True)
    address =models.TextField(null = True, blank = True)
    create_time = models.DateTimeField(auto_now_add = True, null = True, blank =True)
    update_time = models.DateTimeField(auto_now_add = True, null = True, blank =True)
    is_lead = models.BooleanField(default=False)


    class Meta:
        ordering = ['name']


    def __str__(self):
        return f'{self.name},{self.contact},{self.email},{self.school_name},{self.address}'


class Team(models.Model):
    team_name = models.CharField(max_length = 255, unique=True )
    project_idea = models.TextField(null = True, blank = True)
    project_discrapition = models.TextField(null = True, blank = True)
    student = models.ManyToManyField(Student)


    class Meta:
        ordering = ['team_name']

    def __str__(self):
        return f'{self.team_name},{self.project_idea},{self.project_discrapition},{self.student}'


# class Student(models.Model):
#     name = models.CharField(max_length=255, null = True, blank = True)
#     contact = models.CharField(max_length = 12, unique=True)
#     email = models.EmailField(null = True, blank = True)
#     school_name = models.CharField(max_length=255, null = True, blank = True)
#     address =models.TextField(null = True, blank = True)
#     create_time = models.DateTimeField(auto_now_add = True, null = True, blank =True)
#     update_time = models.DateTimeField(auto_now_add = True, null = True, blank =True)
#     is_lead = models.BooleanField(default=False)
#     team = models.ManyToManyField(Team)


#     class Meta:
#         ordering = ['name']


#     def __str__(self):
#         return f'{self.name},{self.contact},{self.email},{self.school_name},{self.address}'