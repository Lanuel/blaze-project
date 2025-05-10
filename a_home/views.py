from django.shortcuts import render
from django.views.generic import TemplateView, ListView
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