from django.db import models
from django.contrib.auth.models import User
 
SEMESTER_NO = ((1, "1st semester"), (2, "2nd semester"), (3, "3rd semester"), 
               (4, "4th semester"), (5, "5th semester"), (6, "6th semester"),
               (7, "7th semester"), (8, "8th semester"))
 
 
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='student')
    roll_no = models.IntegerField(verbose_name="Roll NO")
    registration_no = models.IntegerField(verbose_name="Registration NO")
    session = models.CharField(max_length=10, verbose_name="Session", null=True)

    def __str__(self):
        return self.user.username

 
class Course(models.Model):
    semester_no = models.IntegerField(choices=SEMESTER_NO, verbose_name="Semester NO")
    course_no = models.CharField(max_length=100, verbose_name="Course No")
    course_title = models.CharField(max_length=200, verbose_name="Course Title")
    credit = models.CharField(max_length=100, verbose_name="Credit")

    def __str__(self):
        return self.course_no
 
 
class Registration(models.Model):
    semester_no = models.IntegerField(choices=SEMESTER_NO, verbose_name="Semester NO")
    student = models.ForeignKey(Student, related_name='registrations', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.student.user.username


    

    class Meta:
        unique_together = ('semester_no', 'student')
