from django.db import models

class Address(models.Model):
    city = models.CharField(max_length=50)
    landmark = models.CharField(max_length = 50)
    postal_address = models.CharField(max_length = 225)

    def __str__(self):
        return self.city


class Student(models.Model):
    student_name = models.CharField(max_length= 50)
    standard = models.PositiveIntegerField()
    address = models.ForeignKey(Address,on_delete = models.CASCADE)

    def __str__(self):
        return self.student_name
