from django.urls import path

from . import views

app_name = 'frontpage'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('piece/', views.HomeView.as_view(), name='home'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('thanks/', views.ContactSuccessView.as_view(), name='thanks'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('robots.txt', views.robots, name='robots'),
    path('sitemap.xml', views.SitemapView.as_view(), name='sitemap'),
]
