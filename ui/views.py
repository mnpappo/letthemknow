from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Position
from .tuple_and_dictionaries import *
import requests
import json
from django.db.models import Q
dummy_divisions = ['Barisal', 'Chittagong', 'Dhaka', 'Khulna', 'Mymensingh', 'Rajshahi', 'Rangpur', 'Sylhet']
dummy_safe = [5, 17, 87, 11, 13, 6, 9, 5]
dummy_panicked = [9, 25, 113, 17, 13, 12, 18, 21]
dummy_affected = [0, 1, 7, 2, 0, 1, 0, 0]
dummy_total_user = 400
dummy_total_response = 392


def eng_to_bang(eng_number):
    eng = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    bng = ['১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯', '০']
    eng_number = str(eng_number)
    bng_number = ''
    for i in range(len(eng_number)):
        index = eng.index(eng_number[i])
        bng_number += bng[index]
    return bng_number


def home(request):
    user_id = request.session.get('user_id', 0)
    if user_id == 0:
        position = Position.objects.create()
    else:
        position = Position.objects.get(user_id=user_id)
    request.session['user_id'] = position.user_id

    # total user and response
    total_user = Position.objects.all().count()
    total_response = Position.objects.filter(~Q(state=None)).count()
    print("total user: " + str(total_user))
    print("total_response: "+str(total_response))

    data_1 = []
    data_2 = []
    data_3 = []

    division_list = list(division_code_dic.keys())
    for div in division_list:
        safe_count = Position.objects.filter(division__exact=div, state__exact='1').count()
        panicked_count = Position.objects.filter(division__exact=div, state__exact='2').count()
        affected_count = Position.objects.filter(division__exact=div, state__exact='3').count()
        division_code = division_code_dic[div]
        division_name = div

        # add dummy count #
        index = dummy_divisions.index(div)
        safe_count += dummy_safe[index]
        panicked_count += dummy_panicked[index]
        affected_count += dummy_affected[index]
        # end dummy count #

        a_row = [division_code, division_name, safe_count,
                 'Panicked:' + str(panicked_count) + '<br/ >Affected:' + str(affected_count) + '<br />Safe:' + str(
                     safe_count)]
        data_1.append(a_row)

        b_row = [division_code, division_name, panicked_count,
                 'Panicked:' + str(panicked_count) + '<br/ >Affected:' + str(affected_count) + '<br />Safe:' + str(
                     safe_count)]
        data_2.append(b_row)

        c_row = [division_code, division_name, affected_count,
                 'Panicked:' + str(panicked_count) + '<br/ >Affected:' + str(affected_count) + '<br />Safe:' + str(
                     safe_count)]
        data_3.append(c_row)

    # for data in data_1:
    #   print(data)
    # for data in data_2:
    #   print(data)
    # for data in data_3:
    #     print(data)

    bangladesh_result = (requests.get('https://corona.lmao.ninja/countries/bangladesh')).json()
    # print(bangladesh_result)
    bangladesh_result['cases'] = eng_to_bang(bangladesh_result['cases'])
    bangladesh_result['todayCases'] = eng_to_bang(bangladesh_result['todayCases'])
    bangladesh_result['deaths'] = eng_to_bang(bangladesh_result['deaths'])
    bangladesh_result['todayDeaths'] = eng_to_bang(bangladesh_result['todayDeaths'])
    bangladesh_result['recovered'] = eng_to_bang(bangladesh_result['recovered'])
    bangladesh_result['active'] = eng_to_bang(bangladesh_result['active'])
    bangladesh_result['critical'] = eng_to_bang(bangladesh_result['critical'])
    # print(bangladesh_result)

    world_result = (requests.get('https://corona.lmao.ninja/all')).json()
    # print(world_result)

    world_result['cases'] = eng_to_bang(world_result['cases'])
    world_result['deaths'] = eng_to_bang(world_result['deaths'])
    world_result['recovered'] = eng_to_bang(world_result['recovered'])
    # print(world_result)

    context = {
        'position': position,
        'data1': data_1,
        'data2': data_2,
        'data3': data_3,
        'bangladesh_result': bangladesh_result,
        'world_result': world_result,
        'total_user': total_user+dummy_total_user,              # here dummy data added
        'total_response': total_response+dummy_total_response,  # here dummy data added
    }

    return render(request, 'home.html', context=context)


def info(request):
    bangladesh_result = requests.get('https://corona.lmao.ninja/countries/bangladesh')
    world_result = requests.get('https://corona.lmao.ninja/all')
    context = {
        'bangldesh_result': bangladesh_result.json(),
        'world_result': world_result.json(),
    }
    return render(request, 'info.html', context=context)


def risk_scan(request):
    context = {
        'x': 'hello'
    }
    return render(request, 'apollo_risk_scan.html', context=context)


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
