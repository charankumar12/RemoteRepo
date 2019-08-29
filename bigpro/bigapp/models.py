from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class ServicesData(models.Model):
    course_id=models.IntegerField(primary_key=True)
    course_name=models.CharField(max_length=100,unique=True)
    course_duration=models.CharField(max_length=100)
    course_start_date=models.DateField(max_length=100)
    course_start_time=models.TimeField(max_length=100)
    course_trainer_name=models.CharField(max_length=100)
    course_trainer_exp=models.CharField(max_length=100)

class FeedbackData(models.Model):
    name=models.CharField(max_length=100)
    rating=models.IntegerField()
    date=models.DateTimeField(max_length=100)
    feedback=models.CharField(max_length=500)

class EnquiryData(models.Model):
    Name=models.CharField(max_length=100)
    Mobile=models.BigIntegerField()
    Email=models.EmailField(max_length=100)
    gender=models.CharField(max_length=100)

    COURSES_CHOICES=(
        ('PY',"Python"),
        ('DJ',"Django"),
        ('RA',"Rest-Api"),
        ('FL',"Flask"),
        ('UI',"Ui")
    )
    courses=MultiSelectField(choices=COURSES_CHOICES)

    # SHIFTS_CHOICES=(
    #     ('morning','morningshift'),
    #     ('afternoon','afernoon')
    # )
    # shifts=MultiSelectField(choices=COURSES_CHOICES)










