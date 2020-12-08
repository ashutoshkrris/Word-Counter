from django.http.response import JsonResponse
from django.shortcuts import render
from .counter import start
from .models import SiteList

# Create your views here.


def index(request):
    return render(request, "index.html")


def frequency(request):
    return render(request, "frequency.html")


def result(request):
    if request.method == "POST":
        url_input = request.POST["url_input"]
        try:
            data = SiteList.objects.get(site_name=url_input)
            context = {
                "where": data.location,
                "site_name": data.site_name,
                "result": data.result
            }
            return render(request, "result.html", context)
        except SiteList.DoesNotExist:
            result = start(url_input)
            print(result)
            site_list = SiteList(site_name=url_input, result=result)
            site_list.save()
            context = {
                "where": "Fresh",
                "site_name": url_input,
                "result": result
            }
            return render(request, "result.html", context)
