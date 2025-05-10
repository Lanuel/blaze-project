from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import *


def custom_404(request, exception):
    return render(request, '404.html', status=404)

class HomePageView(ListView):
    model = Post
    template_name = 'a_home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['icons'] = Icon.objects.all
        return context
    

class AboutPageView(TemplateView):
    template_name = "a_home/about.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "a_posts/post_detail.html"
    context_object_name = "post"