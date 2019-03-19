from django.db import models

# Create your models here.
class User(models.Model):
    
    # sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,null=True)
    age = models.IntegerField()
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=32,null=True)


    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name