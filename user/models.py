from django.db import models
from carapp.models import car
# Create your models here.

class Comment (models.Model):
    car = models.ForeignKey(car,on_delete=models.CASCADE,related_name = 'comments')
    name = models.CharField(max_length = 40)
    Comment = models.TextField()
    Created_on = models.DateTimeField(auto_now_add = True,blank = True)


    def __str__(self):
        return f"Comments by {self.name}"