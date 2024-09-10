from django.db import models

class Reservation(models.Model):
    full_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    time = models.TimeField()
    branches = models.CharField(max_length=100)
    date = models.DateField()
    number_of_people = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name
