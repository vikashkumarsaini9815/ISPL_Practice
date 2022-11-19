from django.db import models

# Create your models here.



class Student(models.Model):
    name = models.CharField(max_length=255, null = True, blank = True)
    contact = models.CharField(max_length = 12, unique=True)
    email = models.EmailField(null = True, blank = True)
    school_name = models.CharField(max_length=255, null = True, blank = True)
    address =models.TextField(null = True, blank = True)
    create_time = models.DateTimeField(auto_now_add = True, null = True, blank =True)
    update_time = models.DateTimeField(auto_now_add = True, null = True, blank =True)


    def __str__(self):
        return self.name


class Team(models.Model):
    team_name = models.CharField(max_length = 255, null = True, blank = True)
    project_idea = models.TextField(null = True, blank = True)
    project_discrapition = models.TextField(null = True, blank = True)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return self.team_name