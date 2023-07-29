from django.urls import path
from translate import views

urlpatterns = [
    path('', views.index, name='index'),
    path('translated', views.translated, name='translated'),
    path('speech', views.speech, name="speech"),
]