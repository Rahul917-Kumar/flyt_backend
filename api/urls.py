from django.urls import path
from api.views.health import HealthView
from api.views.drone import DroneListCreateAPIView, DroneDetailAPIView
from api.views.mission import MissionListCreateAPIView, MissionDetailAPIView, PauseMissionAPIView, ResumeMissionAPIView, AbortMissionAPIView

urlpatterns = [
    path('health', HealthView.as_view(), name='test-view'),
    path('drones', DroneListCreateAPIView.as_view(), name='drone-list-create'),
    path('drones/<uuid:pk>', DroneDetailAPIView.as_view(), name='drone-detail'),
    path('missions', MissionListCreateAPIView.as_view(), name='mission-list-create'),
    path('missions/<uuid:pk>', MissionDetailAPIView.as_view(), name='mission-detail'),
    path('missions/<uuid:pk>/pause', PauseMissionAPIView.as_view()),
    path('missions/<uuid:pk>/resume', ResumeMissionAPIView.as_view()),
    path('missions/<uuid:pk>/abort', AbortMissionAPIView.as_view()),
]
