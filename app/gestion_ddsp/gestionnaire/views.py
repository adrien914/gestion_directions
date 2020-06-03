from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from carte.models import Direction
import json


class Gestionnaire(View):

    @staticmethod
    def get(request, direction: str = None):
        if direction:
            direction = Direction.objects.get(map_code=direction)
        all_directions = Direction.objects.all()
        context = {"direction": direction, 'all_directions': all_directions}
        return render(request, "gestionnaire.html", context)

class SearchEngine(View):

    @staticmethod
    def post(request):
        context = {"propositions": []}
        text = request.POST.get("text", "")
        directions = Direction.objects.filter(name__contains=text.upper())
        for direction in directions:
            context["propositions"].append(direction.name)
        return JsonResponse(context)