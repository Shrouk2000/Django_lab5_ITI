
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import TraineeViewSet, trainee_list, trainee_detail, create_trainee, update_trainee, delete_trainee

router = DefaultRouter()
router.register(r'trainees', TraineeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/trainees/', trainee_list, name='trainee_list'),
    path('api/trainees/<int:pk>/', trainee_detail, name='trainee_detail'),
    path('api/trainees/create/', create_trainee, name='create_trainee'),
    path('api/trainees/<int:pk>/update/', update_trainee, name='update_trainee'),
    path('api/trainees/<int:pk>/delete/', delete_trainee, name='delete_trainee'),
]
