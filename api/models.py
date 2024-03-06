from django.db import models

class Profissional(models.Model):


    id = models.AutoField(primary_key=True)
    nome_completo = models.CharField(max_length=100)
    nome_social = models.CharField(max_length=50)
    profissao = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    contato = models.IntegerField()

class Consulta(models.Model):

    id = models.AutoField(primary_key=True)
    id_prof = models.ForeignKey(Profissional, on_delete=models.CASCADE, related_name='id_prof')
    data_consulta = models.CharField(max_length=50)