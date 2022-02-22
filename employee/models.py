from django.db import models

# Create your models here.
class Employee(models.Model):
    ename = ename = models.CharField(max_length=50)
    eage = models.IntegerField()
    eemail = models.EmailField()
    econtact = models.CharField(max_length=55)

    class Meta:
        db_table = 'employee1'
