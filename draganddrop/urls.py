from django.urls import path
from .views import PageBuilderView,HomePageView
urlpatterns = [
path('', HomePageView.as_view(), name='home'),
path('pagebuilder/', PageBuilderView.as_view(), name='pagebuilder'),
]

