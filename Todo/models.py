from binascii import Incomplete
from django.db import models

# Create your models here.
class tsk(models.Model):
    Task = models.CharField(max_length=122)
    status=models.CharField(max_length=100,default='Incomplete'  )

    
    def __str__(self):
        return self.Task
