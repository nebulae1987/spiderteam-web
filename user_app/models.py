from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    create_time = models.DateField(auto_now_add=True)
    remark = models.CharField(max_length=100)          #加密问题与答案
    class Meta:
        db_table='t_user'
