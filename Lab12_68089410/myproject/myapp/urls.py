from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('form/', views.add_person, name='add_person'),
    path('edit/<int:person_id>/', views.edit, name='edit_person'),
    path('delete/<int:person_id>/', views.delete, name='delete_person'),
]