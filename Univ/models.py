from __future__ import unicode_literals

from django.db import models


class Home(models.Model):
    Company_id = models.CharField(max_length=120)
    Company_Name = models.CharField(max_length=120)
    Company_Location = models.CharField(max_length=120)

    def __str__(self):
        return self.Company_Name


class Dept(models.Model):
    Dpt_Name = models.CharField(max_length=120)
    Dpt_loc = models.CharField(max_length=120)
    Dpt_id = models.CharField(max_length=120)


class CompRel(models.Model):
    Company_id = models.ForeignKey(Home, on_delete=models.CASCADE)
    Branch_id = models.CharField(max_length=120)


class StudentInfo(models.Model):
    Sid = models.CharField(max_length=5, null=None, unique=True)
    Name = models.CharField(max_length=120, null=True)
    Dept = models.CharField(max_length=5, null=True)
    Credit = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.Name


class Instructor(models.Model):
    I_Id = models.CharField(max_length=5, primary_key=True)
    Name = models.CharField(max_length=120)
    Dept = models.CharField(max_length=5)
    Salary = models.IntegerField(default=0)

    def __str__(self):
        return self.Name


class Branch(models.Model):
    Branch_id = models.ForeignKey(CompRel, on_delete=models.CASCADE)
    Branch_Name = models.CharField(max_length=120)


CS101 = 'Computer Science Basic'
PY101 = 'Basics of Python'
DJ101 = 'Basics of Django'
AI = 'Artificial Intelligence'
ML = 'Machine Learning'
ES = 'Embedded System'
Auto = 'Automation'

CO = 'Computer Science'
EE = 'Electrical'
EC = 'Electronics and Communications'
CE = 'Civil'
ME = 'Mechanical'
BIO = 'BioTech'
NONE = 'None'

AllCourse = (
    (CS101, 'Computer Science Basic'),
    (PY101, 'Basics of Python'),
    (DJ101, 'Basics of Django'),
    (ML, 'Machine Learning'),
    (AI, 'Artificial Intelligence'),
    (ES, 'Embedded Systems'),
    (Auto, 'Automation'),
)

AllBranch = (
    (CO, 'Computer Science'),
    (EE, 'Electrical'),
    (EC, 'Electronics and Communications'),
    (CE, 'Civil'),
    (ME, 'Mechanical'),
    (BIO, 'BioTech'),
    (NONE, 'None'),
)


class Course(models.Model):
    CourseId = models.CharField(max_length=100,
                                null=True, unique=True)
    CourseName = models.CharField(max_length=100, choices=AllCourse,
                                  blank=True, null=True)
    BranchName = models.CharField(max_length=100,
                                  choices=AllBranch, default='None',
                                  blank=True, null=True)
    Credits = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.CourseName + ' : ' + self.BranchName


class Advisor(models.Model):
    Sid = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    I_Id = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return self.I_Id


class PreReq(models.Model):
    CourseId = models.ForeignKey(Course, on_delete=models.CASCADE)
    PreReq_Id = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.PreReq_Id


class Section(models.Model):
    CourseId = models.ForeignKey(Course, on_delete=models.CASCADE)
    sec_id = models.CharField(unique=True, null=False, max_length=50)






















