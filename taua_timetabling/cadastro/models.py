from django.db import models

# Create your models here.
class Professor(models.Model):
    id = models.IntegerField(db_column='siape', primary_key=True)
    nome = models.CharField(max_length=1024, null=False)
    email = models.EmailField(unique=True)

class Disciplina(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    carga_horaria = models.IntegerField()
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    semestre = models.IntegerField()

