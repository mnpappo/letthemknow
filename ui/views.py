from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Position
from .tuple_and_dictionaries import *

# Create your views here.
# def home(request):
#     template = loader.get_template('home.html')
#     context = {
#         'x': 'hello',
#     }
#     return HttpResponse(template.render(context, request))


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
    lat = float(request.GET.get('lat', None))
    lng = float(request.GET.get('lng', None))
    district = request.GET.get('district')
    division = request.GET.get('division')
    address = request.GET.get('address')
    data = {
    }
    return JsonResponse(data)