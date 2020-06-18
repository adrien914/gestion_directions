

from carte.models import Direction, Hebergement, EtatSite, Contact, Hebergeur
from carte.utils.etat_deploiement import get_paragraph
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from datetime import datetime
import json


class Index(View):


    @staticmethod
    def get(request):
        if not request.user.is_authenticated:
            return render(request, "connection.html")
        directions = Direction.objects.all()
        if len(directions) < 90:
            Direction.generate_all()
            directions = Direction.objects.all()
        regions_colors = {}
        for direction in directions:
            if 'FR-' in direction.map_code:
                regions_colors[direction.map_code] = direction.etat_site.color
        paragraph = get_paragraph()
        context = {'directions': directions, "regions_colors": json.dumps(regions_colors), 'paragraph': paragraph}
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



@csrf_exempt
def insert_csv(request):
    data = json.loads(request.body)
    ddsps = data["ddsps"]
    for ddsp in ddsps:
        direction = Direction.objects.filter(name__contains=ddsp["DDSP"])
        if direction:
            direction = direction[0]
            try:
                for contact in ddsp["contacts"]:
                    Contact.objects.create(**contact, direction=direction)
                for hebergeur in ddsp["hebergeurs"]:
                    Hebergeur.objects.create(**hebergeur, direction=direction)
            except IntegrityError:
                pass
            etat_ddsp = ddsp["etat_site"].replace("\\/", "/").encode().decode('unicode_escape').replace('Ã©', "é").split(" ")
            for etat in etat_ddsp:
                etat_site = EtatSite.objects.filter(name__contains=etat)
                if etat_site:
                    break
            if etat_site:
                direction.etat_site = etat_site[0]
            direction.url_site = ddsp["url_site"]
            direction.version_joomla = ddsp["version_joomla"]
            direction.save()
    return JsonResponse(data)