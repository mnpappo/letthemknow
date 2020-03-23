from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Position
from .tuple_and_dictionaries import *
import requests


class Row:
    def __init__(self, division_code, division_name, safe_count, panicked_count, affected_count ):
        self.division_code = division_code,
        self.division_name = division_name,
        self.safe_count = safe_count,
        self.panicked_count = panicked_count,
        self.affected_count = affected_count,


def home(request):
    user_id = request.session.get('user_id', 0)
    if user_id == 0:
        position = Position.objects.create()
    else:
        position = Position.objects.get(user_id=user_id)
    request.session['user_id'] = position.user_id

    final_list = []
    position_list = Position.objects.all()
    division_list = list(division_code_dic.keys())
    for div in division_list:
        safe_count = Position.objects.filter(division__exact=div, state__exact='1').count()
        panicked_count = Position.objects.filter(division__exact=div, state__exact='2').count()
        affected_count = Position.objects.filter(division__exact=div, state__exact='3').count()
        division_code = division_code_dic[div]
        division_name = div
        row = Row(division_code, division_name, safe_count, panicked_count, affected_count)

        final_list.append(row)


    result = requests.get('https://corona.lmao.ninja/countries/bangladesh')
    print(type(result.json()))
    print(result.json())
    print("total cases " + str(result.json()['cases']))

    context = {
        'position': position,
        'final_list': final_list,
    }

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
        position = Position.objects.create(latitude=lat,
                                           longitude=lng,
                                           state=state,
                                           district=district,
                                           division=division,
                                           address=address,
                                           )
    else:
        print("Etatei")
        position = Position.objects.get(user_id=user_id)
        position.latitude = lat
        position.longitude = lng
        position.state = state
        position.division = division
        position.district = district
        position.address = address
        position.save()
    request.session['user_id'] = position.user_id

    data = {
        'address': position.address,
        'lat': position.latitude,
        'lng': position.longitude,
        'state': position.state,
    }
    return JsonResponse(data)
