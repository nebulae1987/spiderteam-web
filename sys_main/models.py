from django.db import models

# Create your models here.
class Recruit(models.Model):
    position = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    work_addr = models.CharField(max_length=250)
    department = models.CharField(max_length=50)
    job_info = models.TextField()
    class Meta:
        db_table = 't_recruit'
