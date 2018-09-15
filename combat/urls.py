from django.urls import path

from . import views

app_name = 'combat'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('archive/', views.ArchiveView.as_view(), name='archive'),
    path('new/', views.new, name='new'),
    path('<int:character_id>/change/', views.change, name='change'),
    path('add/', views.add, name='add'),
    path('<int:character_id>/delete/', views.delete, name='delete'),
]
