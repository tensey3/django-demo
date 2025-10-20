from django.urls import path
from .views import TopView

app_name = 'mondai1'

urlpatterns = [
    path('', TopView.as_view(), name='top'),
]
