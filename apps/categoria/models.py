from django.db import models

class Categoria(models.Model):
    idC = models.AutoField(primary_key=True)
    nombreC = models.CharField(max_length=50)