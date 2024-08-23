from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_trainee, name='create_trainee'),
    path('<int:id>/', views.detail, name='detail'),
    path('<int:id>/update/', views.update_trainee, name='update_trainee'),
    path('<int:id>/delete/', views.delete_trainee, name='delete_trainee'),
]
