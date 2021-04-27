from django.shortcuts import render

from django.views.generic import TemplateView


class PageBuilderView(TemplateView):
    template_name = 'index.html'

class HomePageView(TemplateView):
    template_name = 'home.html'
