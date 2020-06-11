from django.contrib.auth import authenticate, login
from carte.models import Direction, Hebergement, EtatSite
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
import json


class Index(View):


    @staticmethod
    def get(request):
        if not request.user.is_authenticated:
            return render(request, "connection.html")
        if len(Direction.objects.all()) < 90:
            Direction.generate_all()
        directions = Direction.objects.all()
        regions_colors = {}
        for direction in directions:
            if 'FR-' in direction.map_code:
                regions_colors[direction.map_code] = direction.etat_site.color
        context = {'directions': directions, "regions_colors": json.dumps(regions_colors)}
        return render(request, "index.html", context)

    @staticmethod
    def post(request):
        try:
            data = request.POST
            user = authenticate(request, username=data["username"], password=data["password"])
            if user is not None:
                login(request, user)
                response = JsonResponse({"message": "success"})
                response.status_code = 200
            return response
        except Exception as e:
            print(e)
            response = JsonResponse({"message": "error"})
            response.status_code = 500
            return response


class GenerateDirections(View):

    @staticmethod
    def get(request):
        EtatSite.generate_all()
        Hebergement.generate_all()
        Direction.generate_all()
        return redirect('index')

class GetDdspName(View):

    @staticmethod
    def post(request):
        try:
            map_code = request.POST["code"]
            direction = Direction.objects.get(map_code=map_code)
            return JsonResponse({"code": 200, "name": direction.name})
        except:
            response = JsonResponse({})
            response.status_code = 500
            return response


