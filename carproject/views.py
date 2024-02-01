from django.shortcuts import render 
from carapp.models import car,Brand

def home(request,brand_slug=None):
    data = car.objects.all()

    if brand_slug is not None:
        brand = Brand.objects.get(slug = brand_slug)
        data = car.objects.filter(brand = brand)
    
    brand = Brand.objects.all()

    return render(request,'home.html',{'data':data,'brands':brand})
    