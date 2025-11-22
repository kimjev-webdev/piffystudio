from django.shortcuts import render

def installations(request):
    return render(request, 'portfolio/installations.html')

def digital(request):
    return render(request, 'portfolio/digital.html')

def art(request):
    return render(request, 'portfolio/art.html')

