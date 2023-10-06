from django.db import models


class Producto(models.Model):
    idP = models.AutoField(primary_key=True)
    nombreP = models.CharField(max_length=50)
    descripcionP = models.CharField(max_length=50)
    