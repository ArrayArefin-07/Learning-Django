from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#one to One relationship
class teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=50)
    teacher_id = models.IntegerField()

#Many to One Relationship
class student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=30)
    student_reg = models.IntegerField()

#Many To Many Relationship
class Course(models.Model):
    user = models.ManyToManyField(User)
    course_name = models.CharField(max_length=40)
    course_code = models.IntegerField()
     #for Showing Course_teacher in Database
    def Course_teacher(self):
        return ",".join([str(p) for p in self.user.all()])
