# urls.py в каталоге mysite/store

from django.urls import path
from . import views

urlpatterns = [
    path('paintings/', views.painting_list, name='painting_list'),
    path('add/', views.add_painting, name='add_painting'),
    path('', views.main_menu, name='main'),
    path('delete/<int:id>/', views.delete_painting, name='delete_painting'),
    path('edit/<int:id>/', views.edit_painting, name='edit_painting'),
    path('about/', views.about, name='about'),
    # Другие маршруты для вашего приложения store
]
