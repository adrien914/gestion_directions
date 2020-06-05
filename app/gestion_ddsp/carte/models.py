from django.db import models
from gestionnaire.models import EtatSite


class Hebergement(models.Model):
    type = models.CharField(max_length=255, default=None, null=True)

    def __str__(self):
        return self.type


class Direction(models.Model):
    map_code = models.CharField(unique=True, max_length=255)
    name = models.CharField(unique=True, max_length=255)
    etat_site = models.ForeignKey(to=EtatSite, on_delete=models.CASCADE, default=None, null=True)
    hebergement = models.ForeignKey(to=Hebergement, on_delete=models.CASCADE, default=None, null=True)

    @staticmethod
    def generate_all():
        Direction.create(map_code="FR-01", name="DDSP-01")
        for i in range(3, 96):
            Direction.create(map_code="FR-{:02d}".format(i), name="DDSP-{:02d}".format(i))
        Direction.create(map_code="FR-2A", name="DDSP-2A")
        Direction.create(map_code="FR-2B", name="DDSP-2B")
        Direction.create(map_code="DZPAF", name="DZPAF")
        Direction.create(map_code="DRCPN", name="DRCPN")
        Direction.create(map_code="DCRFPN", name="DCRFPN")

    @staticmethod
    def create(map_code, name):
        try:
            Direction.objects.create(map_code=map_code, name=name)
        except Exception as e:
            print("The direction {} wasn't created because {}".format(name, str(e)))
            return

    def __str__(self):
        return self.name

class Contact(models.Model):
    nom = models.CharField(max_length=255, default=None, null=True, blank=True)
    prenom = models.CharField(max_length=255, default=None, null=True, blank=True)
    email = models.CharField(max_length=255, unique=True, default=None, null=True)
    telephone = models.CharField(max_length=255, default=None, null=True, blank=True)
    autres = models.CharField(max_length=255, default=None, null=True, blank=True)
    direction = models.ForeignKey(to=Direction, on_delete=models.CASCADE)


class Stagiaire(models.Model):
    divers = models.CharField(max_length=255)
    direction = models.ForeignKey(to=Direction, on_delete=models.CASCADE)


class Hebergeur(models.Model):
    nom = models.CharField(max_length=255, default=None, null=True, blank=True)
    prenom = models.CharField(max_length=255, default=None, null=True, blank=True)
    email = models.CharField(max_length=255, unique=True, default=None, null=True)
    telephone = models.CharField(max_length=255, default=None, null=True, blank=True)
    autres = models.CharField(max_length=255, default=None, null=True, blank=True)
    direction = models.ForeignKey(to=Direction, on_delete=models.CASCADE)

    def __str__(self):
        return self.prenom + " " + self.nom



