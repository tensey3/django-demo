from django.urls import path
from . import views

app_name = 'blogapp'

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("blog-detail/<int:pk>/", views.BlogDetailView.as_view(), name='blog_detail'),
]