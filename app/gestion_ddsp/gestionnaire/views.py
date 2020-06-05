from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from carte.models import Direction, Hebergement, Hebergeur, Stagiaire, Contact
from gestionnaire.models import EtatSite
from django.core.exceptions import ObjectDoesNotExist
import json


class Gestionnaire(View):

    @staticmethod
    def get(request, direction: str = None):
        context = {}
        if direction:
            try:
                direction = Direction.objects.get(map_code=direction)
            except ObjectDoesNotExist:
                direction = Direction.objects.get(name=direction)
        all_directions = Direction.objects.all()
        if direction:
            etats_sites = EtatSite.objects.all()
            hebergements = Hebergement.objects.all()
            hebergeurs = Hebergeur.objects.filter(direction=direction)
            contacts = Contact.objects.filter(direction=direction)
            stagiaires = Stagiaire.objects.filter(direction=direction)
            context.update({
                "etats_site": etats_sites,
                "hebergements": hebergements,
                "hebergeurs": hebergeurs,
                "contacts": contacts,
                "stagiaires": stagiaires
            })
        context["direction"] = direction
        return render(request, "gestionnaire.html", context)


class SearchEngine(View):

    @staticmethod
    def post(request):
        """
        Matches directions based on the text sent in the request
        """
        context = {"propositions": []}
        text = request.POST.get("text", "")
        directions = Direction.objects.filter(name__contains=text.upper())
        for direction in directions:
            context["propositions"].append(direction.name)
        return JsonResponse(context)


class ChangeSiteState(View):

    @staticmethod
    def post(request):
        """
        Changes the state of a direction
        we're not using .get() for the request params because we want it to throw an exception if it was not sent
        """
        try:
            direction = request.POST["direction"]  # direction is a string in the request
            direction = Direction.objects.get(name=direction)  # get the direction object corresponding to the name in the request
            state = request.POST["state"]  # get the new state for the direction in the request
            state = EtatSite.objects.get(name=state)  # get the EtatSite corresponding to the name in the request
            direction.etat_site = state  # set the direction's etat_site to it
            print(state)
            direction.save()  # save the changes
            return JsonResponse({"code": 200, "new_state": state.name})
        except Exception as e:
            print("Exception:", str(e))
            response = JsonResponse({"error": str(e)})
            response.status_code = 500
            return response

class ChangeHebergement(View):

    @staticmethod
    def post(request):
        """
        Changes the state of a direction
        we're not using .get() for the request params because we want it to throw an exception if it was not sent
        """
        try:
            direction = request.POST["direction"]  # direction is a string in the request
            direction = Direction.objects.get(name=direction)  # get the direction object corresponding to the name in the request
            type_hebergement = request.POST["type_hebergement"]  # get the new hebergement type for the direction in the request
            hebergement = Hebergement.objects.get(type=type_hebergement)  # get the Hebergement corresponding to the type in the request
            direction.hebergement = hebergement  # set the direction's etat_site to it
            print(hebergement.type)
            direction.save()  # save the changes
            return JsonResponse({"code": 200, "type_hebergement": hebergement.type})
        except Exception as e:
            print("Exception:", str(e))
            response = JsonResponse({"error": str(e)})
            response.status_code = 500
            return response

class createOrModifyHebergeur(View):

    @staticmethod
    def post(request):
        print(request.POST)
        try:
            hebergeur_data = {}
            hebergeur_data["nom"] = request.POST["nom"]
            hebergeur_data["prenom"] = request.POST["prenom"]
            hebergeur_data["email"] = request.POST["email"]
            hebergeur_data["telephone"] = request.POST["telephone"]
            hebergeur_data["autres"] = request.POST["autres"]
        except Exception as e:
            print(e)
            response = JsonResponse({"error": str(e)})
            response.status_code = 500
            return response
        try:
            hebergeur_id = request.POST["hebergeur_id"]
            Hebergeur.objects.filter(id=hebergeur_id).update(**hebergeur_data)
        except:
            direction = Direction.objects.get(id=request.POST["direction"])
            hebergeur = Hebergeur.objects.create(**hebergeur_data, direction=direction)
        response = JsonResponse({"message": "success"})
        response.status_code = 200
        return response