# from django.urls import path
# from . import views

# app_name = 'blogapp'

# urlpatterns = [
#     path("", views.IndexView.as_view(), name='index'),
#     path("blog-detail/<int:pk>/", views.BlogDetailView.as_view(), name='blog_detail'),
#     path("science/", views.ScienceListView.as_view(), name='science_list'),
#     path("dailylife/", views.DailylifeListView.as_view(), name='dailylife_list'),
#     path("music/", views.MusicListView.as_view(), name='music_list'),
# ]
from django.urls import path
from . import views

app_name = "blogapp"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("blog-detail/<int:pk>/", views.BlogDetail.as_view(), name="blog_detail"),
    path("science-list/", views.ScienceView.as_view(), name="science_list"),
    path("dailylife-list/", views.DailylifeView.as_view(), name="dailylife_list"),
    path("music-list/", views.MusicView.as_view(), name="music_list"),
]
