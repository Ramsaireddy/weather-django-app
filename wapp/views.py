from django.shortcuts import render
import urllib.request
import json


# Create your views here.
def Home(request):
    print(request.method)
    if request.method=='POST':
        city=request.POST['city']
        source=urllib.request.urlopen(str('http://api.openweathermap.org/data/2.5/weather?q='+str(city)+'&appid=8b43c50762a2659e357666e7bac46c20')).read()
        list_of_data=json.loads(source)
        print(list_of_data)
        
        
        data = { 
            "name": city,
            
            "country_code": str(list_of_data['sys']['country']), 
            
            "temp": str(round((list_of_data['main']['temp']-273.5),3)) + 'C', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
            "wind": str(list_of_data['wind']['speed'])+"km/h",
            "weather":list_of_data["weather"][0]["main"],
            "lon":list_of_data["coord"]['lon'],
            "lat":list_of_data["coord"]['lat'],
           

        } 
        print(data) 
    else: 
        data ={} 
    return render(request,'wapp/home.html',data)

