from django.shortcuts import render, HttpResponse
from django.views import View
from carte.models import Direction


class Index(View):

    @staticmethod
    def get(request):
        req = request.GET
        test = req.get("test", "")
        data = {'test': test}
        return render(request, "index.html", data)


class GenerateDirections(View):

    @staticmethod
    def get(request):
        Direction.generate_all()
        return render(request, "index.html")