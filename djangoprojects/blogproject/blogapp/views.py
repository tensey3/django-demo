# from django.views.generic import ListView, DetailView
# from .models import BlogPost

# class IndexView(ListView):
#     """トップページのビュー"""
#     template_name = "index.html"
#     context_object_name = "orderby_records"
#     queryset = BlogPost.objects.order_by("-posted_at")

# class BlogDetailView(DetailView):
#     """詳細ページのビュー"""
#     template_name = "post.html"
#     model = BlogPost

# class ScienceListView(ListView):
#     model = BlogPost
#     template_name = 'blogapp/science_list.html'
#     context_object_name = 'blog_list'

#     def get_queryset(self):
#         return BlogPost.objects.filter(category='science').order_by('-posted_at')


# class DailylifeListView(ListView):
#     model = BlogPost
#     template_name = 'blogapp/dailylife_list.html'
#     context_object_name = 'blog_list'

#     def get_queryset(self):
#         return BlogPost.objects.filter(category='dailylife').order_by('-posted_at')


# class MusicListView(ListView):
#     model = BlogPost
#     template_name = 'blogapp/music_list.html'
#     context_object_name = 'blog_list'

#     def get_queryset(self):
#         return BlogPost.objects.filter(category='music').order_by('-posted_at')
from django.views.generic import ListView, DetailView
from .models import BlogPost

class IndexView(ListView):
    template_name = "index.html"
    context_object_name = "orderby_records"
    queryset = BlogPost.objects.order_by("-posted_at")
    paginate_by = 4

class BlogDetail(DetailView):
    template_name = "post.html"
    model = BlogPost

class ScienceView(ListView):
    template_name = "science_list.html"
    context_object_name = "science_records"
    queryset = BlogPost.objects.filter(category='science').order_by("-posted_at")
    paginate_by = 2

class DailylifeView(ListView):
    template_name = "dailylife_list.html"
    context_object_name = "dailylife_records"
    queryset = BlogPost.objects.filter(category='dailylife').order_by("-posted_at")
    paginate_by = 2

class MusicView(ListView):
    template_name = "music_list.html"
    context_object_name = "music_records"
    queryset = BlogPost.objects.filter(category='music').order_by("-posted_at")
    paginate_by = 2
