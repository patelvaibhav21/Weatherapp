
from django.shortcuts import render,HttpResponse
import requests
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'base.html')


def weather(request):

    city= request.GET.get('city')
    # print(city)
    # city='delhi'
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a9d4ed24815c118355a761ce5402a9b1'
    data=requests.get(url).json()
    payload={
        'city':data['name'],
        'weather':data['weather'][0]['main'],
        'keltempeature':data['main']['temp'],
        'ctempeature':int(data['main']['temp']-273),
        'pressure':data['main']['pressure']

    }
    context={'data':payload}
    print(context)

    return render(request,'weather.html',context)

def about(request):
    return render(request,'about.html')

def error(request):
    return render(request,'404page.html')
def errors(request,exception):
    return render(request,'404page.html')
