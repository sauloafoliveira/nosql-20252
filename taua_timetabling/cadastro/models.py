from django.db import models

# Create your models here.
class Professor(models.Model):
    id = models.IntegerField(db_column='siape', primary_key=True)
    nome = models.CharField(max_length=1024, null=False)
    email = models.EmailField(unique=True)


class Curso(models.Model):
    id =  models.AutoField(primary_key=True)
    coordenador = models.ForeignKey(Professor, null=False, on_delete=models.DO_NOTHING)
    nome = models.CharField(unique=True, max_length=1024)
    nivel = models.CharField(max_length=1024)
    
class Disciplina(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    carga_horaria = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    semestre = models.IntegerField()

