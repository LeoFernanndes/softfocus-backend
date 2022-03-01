from django.db import models


# Create your models here.
class ComunicacaoDePerda(models.Model):
    nome_do_produtor = models.CharField(max_length=255)
    email_do_produtor = models.CharField(max_length=255)
    cpf_do_produtor = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    tipo_de_lavoura = models.CharField(max_length=255)
    data_da_colheita = models.DateField(max_length=255)
    evento = models.CharField(max_length=255)
