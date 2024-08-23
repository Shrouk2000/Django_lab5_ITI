from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_track, name='create_track'),
    path('<int:id>/', views.detail, name='detail'),
    path('<int:id>/update/', views.update_track, name='update_track'),
    path('<int:id>/delete/', views.delete_track, name='delete_track'),
]
