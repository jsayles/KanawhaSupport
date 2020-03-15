from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'support/home.html', context)
