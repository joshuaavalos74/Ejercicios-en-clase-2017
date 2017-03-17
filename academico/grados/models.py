from django.db import models
class Grado(models.Model):
	nombres= models.CharField(max_length=200)
	orden= models.IntegerField(default=0)


# Create your models here.
