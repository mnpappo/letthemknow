from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    template = loader.get_template('home.html')
    context = {
        'x': 'hello',
    }
    return HttpResponse(template.render(context, request))


from .models import Position


def index(request):
    user_id = request.session.get('user_id', 0)
    if user_id == 0:
        position = Position.objects.create(latitude=12.3333, longitude=13.4444)
    else:
        position = Position.objects.get(user_id=user_id)

    request.session['user_id'] = position.user_id

    context = {
        'user_id': position.user_id,
    }

    return render(request, 'ui/index.html', context=context)
