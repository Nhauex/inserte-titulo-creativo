from django.db import models

# Create your models here.
# probando D:

class ChecklistItem(models.Model):
    elementos = models.CharField(max_length=200)
    completada = models.BooleanField(default=False)
    fecha = models.DateField(auto_now=True)

    def __str__(self):
        return self.elementos


