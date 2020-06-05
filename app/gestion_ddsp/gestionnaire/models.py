from django.db import models
from colorfield.fields import ColorField

class EtatSite(models.Model):
    name = models.CharField(max_length=255)
    color = ColorField(default="#FFFFFF")

    @staticmethod
    def generate_all():
        EtatSite.objects.create(name="Pas de contacts", color="gray")
        EtatSite.objects.create(name="Pré-Requis", color="red")
        EtatSite.objects.create(name="DEV", color="blue")
        EtatSite.objects.create(name="Terminé", color="green")

    def __str__(self):
        return self.name