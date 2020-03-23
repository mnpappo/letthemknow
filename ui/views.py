from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Position
from .tuple_and_dictionaries import *
import requests


def home(request):
    user_id = request.session.get('user_id', 0)
    if user_id == 0:
        position = Position.objects.create()
    else:
        position = Position.objects.get(user_id=user_id)
    request.session['user_id'] = position.user_id

    final_list = []
    row = []
    row.append('Provinces')
    row.append('City Name')
    row.append('Value')
    row.append('{role: \'tooltip\', p: {html: true}}')
    data_1 = []
    data_2 = []
    data_3 = []
    data_1.append(row)
    data_2.append(row)
    data_3.append(row)
    position_list = Position.objects.all()
    ['BD-A', 'Barisal', 21, 'Panicked:100<br/ >Affected:100 <br />Safe:100'],
    division_list = list(division_code_dic.keys())
    for div in division_list:
        safe_count = Position.objects.filter(division__exact=div, state__exact='1').count()
        panicked_count = Position.objects.filter(division__exact=div, state__exact='2').count()
        affected_count = Position.objects.filter(division__exact=div, state__exact='3').count()
        division_code = division_code_dic[div]
        division_name = div

        a_row = []
        a_row.append(division_code)
        a_row.append(division_name)
        a_row.append(safe_count)
        a_row.append('Panicked:'+str(panicked_count)+'<br/ >Affected:'+str(affected_count)+' <br />Safe:'+str(safe_count))
        data_1.append(a_row)

        b_row = []
        b_row.append(division_code)
        b_row.append(division_name)
        b_row.append(panicked_count)
        b_row.append('Panicked:' + str(panicked_count) + '<br/ >Affected:' + str(affected_count) + ' <br />Safe:' + str(
            safe_count))
        data_2.append(b_row)

        c_row = []
        c_row.append(division_code)
        c_row.append(division_name)
        c_row.append(affected_count)
        c_row.append('Panicked:' + str(panicked_count) + '<br/ >Affected:' + str(affected_count) + ' <br />Safe:' + str(
            safe_count))
        data_3.append(c_row)

    # for data in data_1:
    #   print(data)
    #
    # for data in data_2:
    #   print(data)
    # for data in data_3:
    #     print(data)

    # result = requests.get('https://corona.lmao.ninja/countries/bangladesh')
    # print(type(result.json()))
    # print(result.json())
    # print("total cases " + str(result.json()['cases']))

    context = {
        'position': position,
        'data1': data_1,
        'data2': data_2,
        'data3': data_3,
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
