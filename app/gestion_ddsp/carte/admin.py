from django.contrib import admin
from carte.models import Direction


class AdminDirection(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Direction, AdminDirection)
