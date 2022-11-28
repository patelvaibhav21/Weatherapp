
from django.shortcuts import render,HttpResponse
import requests
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'base.html')


def weather(request):
  
    if request.method=='POST':
        city= request.POST['city']
        # print(city)
        # city='delhi'
        url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a9d4ed24815c118355a761ce5402a9b1'
        jdata=requests.get(url).json()
        print(jdata)
        data={
            'city':jdata['name'],
            'weather':jdata['weather'][0]['main'],
            'keltempeature':jdata['main']['temp'],
            'ctempeature':str(int(jdata['main']['temp']-273))+ '°C',
            'pressure':jdata['main']['pressure']

        }
        
        return render(request,'weather.html',data)
    else:
        data={}
        return render(request,'weather.html',data)
        

def about(request):
    return render(request,'about.html')

def error(request):
    return render(request,'404page.html')
def errors(request,exception):
    return render(request,'404page.html')
