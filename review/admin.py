from django.contrib import admin
from .models import teacher
from .models import student
from .models import Course
# Register your models here.
#One To One Relationship
@admin.register(teacher)
class stdAdmin(admin.ModelAdmin):
    list_display = ['teacher_name','teacher_id','user']

#Many To One Relationship
@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display = ['student_name','student_reg','user']
    

#Many To Many Relationship
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name','course_code','Course_teacher']