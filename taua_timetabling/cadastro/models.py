from django.db import models

# Create your models here.
class Professor(models.Model):
    id = models.IntegerField(db_column='siape', primary_key=True)
    nome = models.CharField(max_length=1024, null=False)
    email = models.EmailField(unique=True)

