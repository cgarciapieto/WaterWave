from django.shortcuts import render

from .models import Musical


def index(request):
    latest_musical_list = Musical.objects.all()
    context = {'latest_musical_list': latest_musical_list}
    return render(request, 'musicapp/index.html', context)