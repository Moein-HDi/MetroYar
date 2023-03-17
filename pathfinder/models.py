from django.db import models
from pathfinder.subway import subway
# Create your models here.
class path(models.Model):
    origin = models.TextField()
    destination = models.TextField()
    
    def __str__(self):
        return str('سفر از ایستگاه {ori} به ایستگاه {des}'.format(ori=self.origin, des=self.destination))