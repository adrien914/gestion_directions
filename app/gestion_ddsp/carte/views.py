from django.shortcuts import render, HttpResponse
from django.views import View
from carte.models import Direction


class Index(View):

    @staticmethod
    def get(request):
        if len(Direction.objects.all()) < 90:
            Direction.generate_all()
        req = request.GET
        test = req.get("test", "")
        data = {'test': test}
        return render(request, "index.html", data)


class GenerateDirections(View):

    @staticmethod
    def get(request):
        Direction.generate_all()
        return render(request, "index.html")