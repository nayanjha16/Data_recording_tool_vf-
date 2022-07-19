from django.db import models
from django.contrib.auth.models import User


class users(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=10)
    age = models.IntegerField(default=0)
    contact = models.CharField(max_length=10)
    lang_fluent_in = models.CharField(max_length=50)
    disability = models.CharField(max_length=150)

    def __str__(self):
        return self.f_name + " " + self.l_name
