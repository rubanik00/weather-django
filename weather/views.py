import requests
import os
from dotenv import load_dotenv
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import City
from .forms import CityForm


def index(request):
    appId = os.getenv('APP_ID')
    appId = str(appId)
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appId

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    all_cities = []
    
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'id': city.id,
            'city' : city.name,
            'temp' : res["main"]["temp"],
            'icon' : res["weather"][0]["icon"]
        }
        all_cities.append(city_info)

    contex = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', contex)

def delete(request, id):
        city = City.objects.get(id=id)
        city.delete()
        return HttpResponseRedirect("/")
