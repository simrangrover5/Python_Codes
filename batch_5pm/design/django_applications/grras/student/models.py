from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    dob = models.DateTimeField(null=True)
    ph_no = models.CharField(max_length=15,null=True)
    email = models.EmailField(),
    password = models.CharField(max_length=15,null=False,default='1234567890')
    #address = models.ForeignKey(Address,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Address(models.Model):
    hno = models.CharField(max_length=10)
    street_addr = models.CharField(max_length=60)
    city  = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    pin_code = models.IntegerField()
    sid = models.ForeignKey(Student,on_delete=models.CASCADE)
    def __str__(self):
        addr = self.hno+','+self.street_addr+','+self.city\
        +','+self.state+', '+self.country
        return addr

class Faculty(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=50)
    ph_no = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Course(models.Model):
    roll_no = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.CharField(max_length=50)
    fees = models.FloatField(max_length=6)
    due = models.FloatField(max_length=6)
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    def __str__(self):
        return self.course
