from django.shortcuts import render

def shop_index(request):
    return render(request, 'shop/shop_index.html')
