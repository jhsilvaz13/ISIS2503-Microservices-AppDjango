from .models import Place
from django.http import HttpResponse
from django.http import JsonResponse


import json

def PlaceList(request):
    queryset = Place.objects.all()
    context = list(queryset.values('id', 'name'))
    return JsonResponse(context, safe=False)

def PlaceCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        variable = Place()
        variable.name = data_json["name"]
        variable.save()
        return HttpResponse("successfully created variable")
    
def check(request):
    name=request.data['name']
    place = Place.objects.filter(name=name)
    if place.exists():
        return HttpResponse("Place exists")
    else:
        return HttpResponse("Place does not exist")