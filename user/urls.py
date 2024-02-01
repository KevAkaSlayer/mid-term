from django.urls import path
from . import views

urlpatterns = [
     path('signup/',views.SignUp.as_view(),name = 'signup'),
    path('login/',views.user_login.as_view(),name = 'login'),
    path('logout/',views.user_logout,name = 'logout'),
    path('updatedata/<int:id>',views.updatedata.as_view(),name = 'update'),
    path('passchnge/',views.passchnge,name = 'passchng'),
    path('profile/',views.Profile,name = 'profile'),
]