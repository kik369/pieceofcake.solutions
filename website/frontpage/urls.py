from django.urls import path

from . import views

app_name = 'frontpage'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('piece/', views.PieceView.as_view(), name='piece'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('thanks/', views.ContactSuccessView.as_view(), name='thanks'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('test/', views.TestView.as_view(), name='test'),
]
