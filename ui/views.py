from django.shortcuts import render
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
