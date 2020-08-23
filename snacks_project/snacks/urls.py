from django.urls import path
from .views import HomePageView, AboutPageView, FansPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('fans/', FansPageView.as_view(), name='fans'),
]
