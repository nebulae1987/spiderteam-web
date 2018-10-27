from django.db import models

# Create your models here.
class Recruit(models.Model):
    position = models.Field(max_length=255)
    salary = models.Field(max_length=255)
    company = models.Field(max_length=255)
    experience = models.Field(max_length=255)
    education = models.Field(max_length=255)
    work_addr = models.Field(max_length=255)
    company_size = models.Field(max_length=255)
    job_info = models.TextField(max_length=255)
    main_business = models.Field(max_length=255)
    com_net = models.Field()
    department = models.Field(max_length=255)
    job_requirements = models.TextField()
    status = models.Field(max_length=255)
    create_time = models.Field(max_length=255)
    class Meta:

        db_table='t_recruit'
