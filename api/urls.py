from django.urls import path
from api.views.health import HealthView
from api.views.drone import DroneListCreateAPIView, DroneDetailAPIView
urlpatterns = [
    path('health', HealthView.as_view(), name='test-view'),
    path('drones', DroneListCreateAPIView.as_view(), name='drone-list-create'),
    path('drones/<str:pk>', DroneDetailAPIView.as_view(), name='drone-detail'),
]
