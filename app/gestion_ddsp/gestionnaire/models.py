from django.db import models

class EtatSite(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)

    @staticmethod
    def generate_all():
        EtatSite.objects.create(name="Pas de contacts", color="gray")
        EtatSite.objects.create(name="Pré-Requis", color="red")
        EtatSite.objects.create(name="DEV", color="blue")
        EtatSite.objects.create(name="Terminé", color="green")

    def __str__(self):
        return self.name