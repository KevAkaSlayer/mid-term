from django.urls import path
from . import views
urlpatterns = [
    path('buy/<int:id>', views.buy,name = 'buy'),
    path('detail/<int:id>', views.detail,name = 'detail'),
]