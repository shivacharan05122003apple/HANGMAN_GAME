from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('add',views.add),
    path('check',views.check),
    path('playgame',views.pickword),
    path('CLUE',views.clue)
]