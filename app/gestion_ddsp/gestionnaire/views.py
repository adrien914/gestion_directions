from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from carte.models import Direction, Hebergement, Hebergeur, Stagiaire, Contact, EtatSite, Deplacement
from django.core.exceptions import ObjectDoesNotExist


class Gestionnaire(View):

    @staticmethod
    def get(request, direction: str = None):
        if not request.user.is_authenticated:
            return redirect('login')
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
            try:
                stagiaire = Stagiaire.objects.get(direction=direction)
            except ObjectDoesNotExist:
                stagiaire = None
            context.update({
                "etats_site": etats_sites,
                "hebergements": hebergements,
                "hebergeurs": hebergeurs,
                "contacts": contacts,
                "stagiaire": stagiaire
            })
        context["direction"] = direction
        return render(request, "gestionnaire.html", context)


class Deplacements(View):

    @staticmethod
    def get(request):
        deplacements = Deplacement.objects.all()
        context = { "deplacements": deplacements }
        return render(request, 'deplacement.html', context)


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
            if request.user.is_superuser:
                direction = request.POST["direction"]  # direction is a string in the request
                direction = Direction.objects.get(name=direction)  # get the direction object corresponding to the name in the request
                state = request.POST["state"]  # get the new state for the direction in the request
                state = EtatSite.objects.get(name=state)  # get the EtatSite corresponding to the name in the request
                direction.etat_site = state  # set the direction's etat_site to it
                direction.save()  # save the changes
                return JsonResponse({"code": 200, "new_state": state.name})
            else:
                response = JsonResponse({"error": "not authorized"})
                response.status_code = 401
                return response
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
            if request.user.is_superuser:
                direction = request.POST["direction"]  # direction is a string in the request
                direction = Direction.objects.get(name=direction)  # get the direction object corresponding to the name in the request
                type_hebergement = request.POST["type_hebergement"]  # get the new hebergement type for the direction in the request
                hebergement = Hebergement.objects.get(type=type_hebergement)  # get the Hebergement corresponding to the type in the request
                direction.hebergement = hebergement  # set the direction's etat_site to it
                print(hebergement.type)
                direction.save()  # save the changes
                return JsonResponse({"code": 200, "type_hebergement": hebergement.type})
            else:
                response = JsonResponse({"error": "not authorized"})
                response.status_code = 401
                return response
        except Exception as e:
            print("Exception:", str(e))
            response = JsonResponse({"error": str(e)})
            response.status_code = 500
            return response

class createOrModifyHebergeur(View):

    @staticmethod
    def post(request):
        if request.user.is_superuser:
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
                hebergeur_data["id"] = hebergeur.id
            response = JsonResponse({"message": "success", "hebergeur_data": hebergeur_data})
            response.status_code = 200
            return response
        else:
            response = JsonResponse({"error": "not authorized"})
            response.status_code = 401
            return response

class DeleteHebergeur(View):

    @staticmethod
    def post(request):
        try:
            if request.user.is_superuser:
                data = request.POST
                hebergeur = Hebergeur.objects.get(id=data["id"])
                hebergeur.delete()
                response = JsonResponse({"message": "successfully deleted hebergeur"})
                response.status_code = 200
                return response
            else:
                response = JsonResponse({"error": "not authorized"})
                response.status_code = 401
                return response
        except Exception as e:
            print(e)
            response = JsonResponse({"error": str(e)})
            response.status_code = 500
            return response

class createOrModifyContact(View):

    @staticmethod
    def post(request):
        if request.user.is_superuser:
            try:
                contact_data = {}
                contact_data["nom"] = request.POST["nom"]
                contact_data["prenom"] = request.POST["prenom"]
                contact_data["email"] = request.POST["email"]
                contact_data["telephone"] = request.POST["telephone"]
                contact_data["autres"] = request.POST["autres"]
            except Exception as e:
                print(e)
                response = JsonResponse({"error": str(e)})
                response.status_code = 500
                return response
            try:
                contact_id = request.POST["contact_id"]
                Contact.objects.filter(id=contact_id).update(**contact_data)
            except:
                direction = Direction.objects.get(id=request.POST["direction"])
                contact = Contact.objects.create(**contact_data, direction=direction)
                contact_data["id"] = contact.id
            response = JsonResponse({"message": "success", "contact_data": contact_data})
            response.status_code = 200
            return response
        else:
            response = JsonResponse({"error": "not authorized"})
            response.status_code = 401
            return response

class DeleteContact(View):

    @staticmethod
    def post(request):
        try:
            if request.user.is_superuser:
                data = request.POST
                contact = Contact.objects.get(id=data["id"])
                contact.delete()
                response = JsonResponse({"message": "successfully deleted contact"})
                response.status_code = 200
                return response
            else:
                response = JsonResponse({"error": "not authorized"})
                response.status_code = 401
                return response
        except Exception as e:
            print(e)
            response = JsonResponse({"error": str(e)})
            response.status_code = 500
            return response

class SaveStagiaire(View):

    @staticmethod
    def post(request):
        try:
            if request.user.is_superuser:
                data = request.POST
                direction = Direction.objects.get(id=data["direction_id"])
                try:
                    stagiaire = Stagiaire.objects.get(direction=direction)
                except:
                    stagiaire = Stagiaire.objects.create(direction=direction)
                stagiaire.divers = data["text"]
                stagiaire.save()
                response = JsonResponse({"message": "successfully deleted contact"})
                response.status_code = 200
                return response
            else:
                response = JsonResponse({"error": "not authorized"})
                response.status_code = 401
                return response
        except Exception as e:
            print(e)
            response = JsonResponse({"error": str(e)})
            response.status_code = 500
            return response


class SaveUrl(View):

    @staticmethod
    def post(request):
        try:
            if request.user.is_superuser:
                data = request.POST
                direction = Direction.objects.get(id=data["direction_id"])
                direction.url_site = data["text"]
                direction.save()
                response = JsonResponse({"message": "successfully changed url"})
                response.status_code = 200
                return response
            else:
                response = JsonResponse({"error": "not authorized"})
                response.status_code = 401
                return response
        except Exception as e:
            print(e)
            response = JsonResponse({"error": str(e)})
            response.status_code = 500
            return response


class SaveVersion(View):

    @staticmethod
    def post(request):
        try:
            if request.user.is_superuser:
                data = request.POST
                direction = Direction.objects.get(id=data["direction_id"])
                direction.version_joomla = data["text"]
                direction.save()
                response = JsonResponse({"message": "successfully changed joomla version"})
                response.status_code = 200
                return response
            else:
                response = JsonResponse({"error": "not authorized"})
                response.status_code = 401
                return response
        except Exception as e:
            print(e)
            response = JsonResponse({"error": str(e)})
            response.status_code = 500
            return response

class CreateDdsp(View):

    @staticmethod
    def post(request):
        try:
            if request.user.is_superuser:
                name = request.POST["name"]
                Direction.create(name=name, map_code=name)
                return JsonResponse({"code": 200})
            else:
                response = JsonResponse({"error": "not authorized"})
                response.status_code = 401
                return response
        except:
            response = JsonResponse({})
            response.status_code = 500
            return response


class RemoveDdsp(View):

    @staticmethod
    def post(request):
        try:
            if request.user.is_superuser:
                name = request.POST["name"]
                Direction.objects.get(name=name).delete()
                return JsonResponse({"code": 200})
            else:
                response = JsonResponse({"error": "not authorized"})
                response.status_code = 401
                return response
        except:
            response = JsonResponse({})
            response.status_code = 500
            return response


class createOrModifyDeplacement(View):

    @staticmethod
    def post(request):
        if request.user.is_superuser:
            try:
                # Format the data received to the deplacement's format
                deplacement_data = {}
                deplacement_data["destination"] = request.POST["destination"]
                deplacement_data["date"] = request.POST["date"]
                deplacement_data["commentaires"] = request.POST["commentaires"]
            except Exception as e:
                print(e)
                response = JsonResponse({"error": str(e)})
                response.status_code = 500
                return response
            try:
                # Try to get a deplacement id if it doesn't find one that means it's a new deplacement
                deplacement_id = request.POST["deplacement_id"]
                Deplacement.objects.filter(id=deplacement_id).update(**deplacement_data)
            except:
                # create a new deplacement
                user = request.user
                deplacement = Deplacement.objects.create(**deplacement_data, user=user)
                deplacement_data["id"] = deplacement.id
            response = JsonResponse({"message": "success", "deplacement_data": deplacement_data})
            response.status_code = 200
            return response
        else:
            response = JsonResponse({"error": "not authorized"})
            response.status_code = 401
            return response


class DeleteDeplacement(View):

    @staticmethod
    def post(request):
        try:
            if request.user.is_superuser:
                data = request.POST
                deplacement = Deplacement.objects.get(id=data["id"])
                deplacement.delete()
                response = JsonResponse({"message": "successfully deleted hebergeur"})
                response.status_code = 200
                return response
            else:
                response = JsonResponse({"error": "not authorized"})
                response.status_code = 401
                return response
        except Exception as e:
            print(e)
            response = JsonResponse({"error": str(e)})
            response.status_code = 500
            return response