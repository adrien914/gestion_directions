from django.contrib import admin
from carte.models import Direction, Contact, Stagiaire, Hebergeur, Hebergement


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


admin.site.register(Direction, AdminDirection)
admin.site.register(Contact, AdminContact)
admin.site.register(Stagiaire, AdminStagiaire)
admin.site.register(Hebergeur, AdminHebergeur)
admin.site.register(Hebergement, AdminHebergement)