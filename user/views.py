from django.shortcuts import render,redirect
from .forms import UserForm,ChangeData
from django.urls import reverse_lazy
from django.contrib.auth import logout,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.generic import CreateView,UpdateView
# Create your views here.


class SignUp(CreateView):
    model = User
    template_name = 'signup.html'
    form_class = UserForm
    success_url = reverse_lazy('login')

class user_login(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    def form_valid(self, form):
        return super().form_valid(form)
    def form_invalid(self, form):
        return super().form_invalid(form)
@method_decorator(login_required(login_url='login'),name = 'dispatch')  
class updatedata(UpdateView):
    model = User
    form_class = ChangeData
    template_name = 'chngedata.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'

@login_required(login_url='login')
def Profile(request):
    return render(request,'profile.html')

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect ('login')

@login_required(login_url='login')
def passchnge(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user = request.user,data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect ('profile')
    else :
        form = PasswordChangeForm(user = request.user)
    return render(request,'chngepass.html',{'form':form})

