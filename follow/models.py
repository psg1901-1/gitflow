from django.db import models

class Follow(models.Model):
    uid=models.IntegerField()
    fid=models.IntegerField()
    time=models.DataTimeField(auto_now_add=True) 
