from django.urls import path
from . import views

app_name='mondai2'
urlpatterns=[
    path('', views.StartView.as_view(), name='start')
]