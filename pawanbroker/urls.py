from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('display_intrest', views.display_intrest,name='display_intrest')
]