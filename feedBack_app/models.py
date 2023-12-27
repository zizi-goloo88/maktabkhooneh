import datetime

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class FeedBack(models.Model):
    text = models.CharField(max_length=200)
    rate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.now() , blank=True)

# Create your models here.
