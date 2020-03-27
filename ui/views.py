from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Position, Stat
from .tuple_and_dictionaries import *
import requests
import json
from django.db.models import Q
from datetime import datetime
from datetime import timedelta
from django.utils import timezone


dummy_divisions = ['Barisal', 'Chittagong', 'Dhaka', 'Khulna', 'Mymensingh', 'Rajshahi', 'Rangpur', 'Sylhet']
dummy_safe = [5, 17, 87, 11, 13, 6, 9, 5]
dummy_panicked = [9, 25, 113, 17, 13, 12, 18, 21]
dummy_affected = [0, 1, 7, 2, 0, 1, 0, 0]
dummy_total_user = 400
dummy_total_response = 392


def eng_to_bang(eng_number):
    """
    translate english digit to bangla digit
    :param eng_number:
    :return: bng_number
    """
    eng = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    bng = ['১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯', '০']
    eng_number = str(eng_number)
    bng_number = ''
    for i in range(len(eng_number)):
        index = eng.index(eng_number[i])
        bng_number += bng[index]
    return bng_number


def home(request):
    """
    Home view of Let them know app.
    :param request: nothing
    :return: position, bangladesh_stat, world_stat
    """
    # check user is old or new using previous session data. if new, set the user_id to the session.
    user_id = request.session.get('user_id', 0)
    if user_id == 0:
        position = Position.objects.create()
    else:
        position = Position.objects.get(user_id=user_id)
    request.session['user_id'] = position.user_id

    # total user and response
    total_user = Position.objects.all().count()
    total_response = Position.objects.filter(~Q(state=None)).count()

    # generate the data for division wise safe, panicked and affected number for template
    data_1 = []        # safe list
    data_2 = []        # panicked list
    data_3 = []        # affected list

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

    # get and prepared the statistic of corona virus from 'https://corona.lmao.ninfa/' api.
    # get the stat from database
    stat, created = Stat.objects.get_or_create(id=1)
    # try api fro bangladesh result
    try:
        bangladesh_result = (requests.get('https://corona.lmao.ninja/countries/bangladesh'))
    except Exception as e:
        print(e)
        # get the data from the database
        bangladesh_result = stat.bangladesh_result
        # replace the single quote(') with double quote(") for string to json conversion
        # string dictionary can't be converted to json if key-value are confined with single quote(')
        bangladesh_result = bangladesh_result.replace("'", '"')
        bangladesh_result = json.loads(bangladesh_result)

    if bangladesh_result.status_code and bangladesh_result.status_code == 200:
        bangladesh_result = bangladesh_result.json()
        if created:
            stat.bangladesh_result = bangladesh_result
            stat.save()
        if stat.update_time + timedelta(minutes=10) < timezone.now():
            stat.bangladesh_result = bangladesh_result
            stat.save()
    else:
        bangladesh_result = stat.bangladesh_result
        bangladesh_result = bangladesh_result.replace("'", '"')
        bangladesh_result = json.loads(bangladesh_result)

    # Translate English Digit to Bangla digit for Bangladesh result
    bangladesh_result['cases'] = eng_to_bang(bangladesh_result['cases'])
    bangladesh_result['todayCases'] = eng_to_bang(bangladesh_result['todayCases'])
    bangladesh_result['deaths'] = eng_to_bang(bangladesh_result['deaths'])
    bangladesh_result['todayDeaths'] = eng_to_bang(bangladesh_result['todayDeaths'])
    bangladesh_result['recovered'] = eng_to_bang(bangladesh_result['recovered'])
    bangladesh_result['active'] = eng_to_bang(bangladesh_result['active'])
    bangladesh_result['critical'] = eng_to_bang(bangladesh_result['critical'])

    # try api for world_result
    try:
        world_result = requests.get('https://corona.lmao.ninja/all')
    except Exception as e:
        world_result = stat.world_result
        world_result = world_result.replace("'", '"')
        world_result = json.loads(bangladesh_result)

    if world_result.status_code and world_result.status_code == 200:
        world_result = world_result.json()
        a = stat.update_time.time()
        b = stat.update_time + timedelta(minutes=10)
        c = timezone.now()
        d = b - c
        if created:
            stat.world_result = world_result
            stat.save()
        if stat.update_time + timedelta(minutes=10) < timezone.now():
            stat.world_result = world_result
            stat.save()
    else:
        world_result = stat.world_result
        world_result = world_result.replace("'", '"')
        world_result = json.loads(world_result)

    # Translate English Digit to Bangla digit for Bangladesh result
    world_result['cases'] = eng_to_bang(world_result['cases'])
    world_result['deaths'] = eng_to_bang(world_result['deaths'])
    world_result['recovered'] = eng_to_bang(world_result['recovered'])

    context = {
        'position': position,
        'data1': data_1,
        'data2': data_2,
        'data3': data_3,
        'bangladesh_result': bangladesh_result,
        'world_result': world_result,
        'total_user': total_user + dummy_total_user,  # here dummy data added
        'total_response': total_response + dummy_total_response,  # here dummy data added
    }

    return render(request, 'home.html', context=context)


def stat_view(request):
    """
    prepared and send bangladesh and world stat of corona virus to the template
    :param request:
    :return: bangladesh_result, world_result in context
    """
    # get and prepared the statistic of corona virus from 'https://corona.lmao.ninfa/' api.
    stat, created = Stat.objects.get_or_create(id=1)  # get the stat from database
    # try api fro bangladesh result
    try:
        bangladesh_result = (requests.get('https://corona.lmao.ninja/countries/bangladesh'))
    except Exception as e:
        print(e)
        # get the data from the database
        bangladesh_result = stat.bangladesh_result
        # replace the single quote(') with double quote(") for string to json conversion
        # string dictionary can't be converted to json if key-value are confined with single quote(')
        bangladesh_result = bangladesh_result.replace("'", '"')
        bangladesh_result = json.loads(bangladesh_result)

    if bangladesh_result.status_code and bangladesh_result.status_code == 200:
        bangladesh_result = bangladesh_result.json()
        if created:
            stat.bangladesh_result = bangladesh_result
            stat.save()
        if stat.update_time + timedelta(minutes=10) < timezone.now():
            stat.bangladesh_result = bangladesh_result
            stat.save()
    else:
        bangladesh_result = stat.bangladesh_result
        bangladesh_result = bangladesh_result.replace("'", '"')
        bangladesh_result = json.loads(bangladesh_result)

    # Translate English Digit to Bangla digit for Bangladesh result
    bangladesh_result['cases'] = eng_to_bang(bangladesh_result['cases'])
    bangladesh_result['todayCases'] = eng_to_bang(bangladesh_result['todayCases'])
    bangladesh_result['deaths'] = eng_to_bang(bangladesh_result['deaths'])
    bangladesh_result['todayDeaths'] = eng_to_bang(bangladesh_result['todayDeaths'])
    bangladesh_result['recovered'] = eng_to_bang(bangladesh_result['recovered'])
    bangladesh_result['active'] = eng_to_bang(bangladesh_result['active'])
    bangladesh_result['critical'] = eng_to_bang(bangladesh_result['critical'])

    # try api for world_result
    try:
        world_result = requests.get('https://corona.lmao.ninja/all')
    except Exception as e:
        print(e)
        world_result = stat.world_result
        world_result = world_result.replace("'", '"')
        world_result = json.loads(world_result)

    if world_result.status_code and world_result.status_code == 200:
        world_result = world_result.json()
        if created:
            stat.world_result = world_result
            stat.save()
        if stat.update_time + timedelta(minutes=10) < timezone.now():
            stat.world_result = world_result
            stat.save()
    else:
        world_result = stat.world_result
        world_result = world_result.replace("'", '"')
        world_result = json.loads(world_result)

    # Translate English Digit to Bangla digit for Bangladesh result
    world_result['cases'] = eng_to_bang(world_result['cases'])
    world_result['deaths'] = eng_to_bang(world_result['deaths'])
    world_result['recovered'] = eng_to_bang(world_result['recovered'])

    context = {
        'bangladesh_result': bangladesh_result,
        'world_result': world_result,
    }
    return render(request, 'info.html', context=context)


def risk_scan(request):
    context = {
        'x': 'hello'
    }
    return render(request, 'apollo_risk_scan.html', context=context)


def update(request):
    """
    Update user's location, address, state, district and division data
    :param request:
    :return: state, lat, lng, district, division, address
    """
    state = request.GET.get('state')
    lat = float(request.GET.get('lat'))
    lng = float(request.GET.get('lng'))
    district = request.GET.get('district')
    division = request.GET.get('division')
    address = request.GET.get('address')
    division = division.split()[0]
    district = district.split()[0]

    user_id = request.session.get('user_id', None)
    if user_id is None:
        position = Position.objects.create(latitude=lat,
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
        position.save()
    request.session['user_id'] = position.user_id

    data = {
        'address': position.address,
        'lat': position.latitude,
        'lng': position.longitude,
        'state': position.state,
    }
    return JsonResponse(data)
