from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News

# Create your views here.

class NewsListView(ListView):
    queryset = News.objects.all()
    template_name = "news/noticias.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewsListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
