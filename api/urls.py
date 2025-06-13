from django.urls import path
from api.views.health import HealthView

urlpatterns = [
    path('health', HealthView.as_view(), name='test-view'),
]
