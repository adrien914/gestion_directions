from django.contrib import admin
from gestionnaire.models import EtatSite
# Register your models here.

class AdminEtatSite(admin.ModelAdmin):
    list_display = ["name", "color"]

admin.site.register(EtatSite, AdminEtatSite)