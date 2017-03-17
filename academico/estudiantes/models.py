from django.db import models
class Estudiante(models.Model):
	nombre= models.CharField(max_length=200)
	apellido= models.CharField(max_length=200)
	edad= models.IntegerField(default=0)
	grado= models.ForeignKey('grados.Grado')

	def __unicode__(self):
		return "%S %S %S - %S" % (
			self.nombre,
			self.apellido,
			self.edad,
			self.grado)
# Create your models here.
