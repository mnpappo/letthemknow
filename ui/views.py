from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Position
from .tuple_and_dictionaries import *


def home(request):
    user_id = request.session.get('user_id', 0)
    if user_id == 0:
        position = Position.objects.create(latitude=12.3333, longitude=13.4444)
    else:
        position = Position.objects.get(user_id=user_id)
    request.session['user_id'] = position.user_id
    context = {
        'user_id': position.user_id,
    }
    print(division_code_dic)
    print(district_code_dic)
    print(district_division_dic)
    return render(request, 'home.html', context=context)


def update(request):
    state = request.GET.get('state')
    lat = float(request.GET.get('lat'))
    lng = float(request.GET.get('lng'))
    district = request.GET.get('district')
    division = request.GET.get('division')
    address = request.GET.get('address')
    division = division.split()[0]
    district = district.split()[0]

    user_id = request.session.get('user_id', None)
    if user_id == None:
        position = Position.objects.create(user_id=user_id,
                                           latitude=lat,
                                           longitude=lng,
                                           state=state,
                                           district=district,
                                           division=division,
                                           address=address,
                                           )
    else:
        position = Position.objects.get(user_id=user_id)
        position.latitude = lat
        position.longitude = lng
        position.state = state
        position.division = division
        position.district = district
        position.address = address
    request.session['user_id'] = position.user_id

    data = {
        'address': position.address,
        'lat': position.latitude,
        'lng': position.longitude,
        'state': position.state,
    }
    return JsonResponse(data)