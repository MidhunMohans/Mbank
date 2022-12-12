from django.db import models


# Create your models here.
class Detail(models.Model):
    name = models.CharField(max_length=250)
    address = models.TextField()
    date = models.DateTimeField()
    age= models.IntegerField()
    phone_num=models.IntegerField()
    email = models.EmailField(max_length=70)

    def __str__(self):
        return self.name


