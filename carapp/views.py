from django.shortcuts import render,redirect
from .models import car
from django.contrib.auth.decorators import login_required
from user.forms import CommentForm
from user.models import Comment
# Create your views here.


def detail(request,id):
    carr = car.objects.get(pk=id)
    comments = Comment.objects.filter(car = carr)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = carr
            comment.save()
            return redirect('details',id = id)
    else :
        form = CommentForm()
    return render (request,'cardetail.html',{'car':carr,'form':form,'comment':comments})

def buy(request,id):
    carr = car.objects.get(pk = id)
    carr.quantity = carr.quantity - 1
    carr.save()
    request.user.bought_cars.add(carr)
    return render (request,'cardetail.html',{'car':carr})
