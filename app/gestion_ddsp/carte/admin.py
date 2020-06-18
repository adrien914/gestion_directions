from django.contrib import admin
from carte.models import Direction, Contact, Stagiaire, Hebergeur, Hebergement, EtatSite, Deplacement


class AdminDirection(admin.ModelAdmin):
    list_display = ["name", "etat_site"]


class AdminContact(admin.ModelAdmin):
    list_display = ["email", "nom", "prenom"]


class AdminStagiaire(admin.ModelAdmin):
    list_display = ["direction"]


class AdminHebergeur(admin.ModelAdmin):
    list_display = ["email", "nom", "prenom"]


class AdminHebergement(admin.ModelAdmin):
    list_display = ["type"]

class AdminEtatSite(admin.ModelAdmin):
    list_display = ["name", "color"]

class AdminDeplacement(admin.ModelAdmin):
    list_display = ["destination", "date"]

admin.site.register(EtatSite, AdminEtatSite)
admin.site.register(Direction, AdminDirection)
admin.site.register(Contact, AdminContact)
admin.site.register(Stagiaire, AdminStagiaire)
admin.site.register(Hebergeur, AdminHebergeur)
admin.site.register(Hebergement, AdminHebergement)
admin.site.register(Deplacement, AdminDeplacement)