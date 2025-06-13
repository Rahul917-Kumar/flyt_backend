from django.db import models
import uuid

class Drone(models.Model):
    STATUS_CHOICES = [
        ("available", "Available"),
        ("in_mission", "In Mission"),
        ("charging", "Charging"),
        ("maintenance", "Maintenance")
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="available")
    battery_level = models.IntegerField(default=100)
    location = models.JSONField(null=True, blank=True)
    last_heartbeat = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Drone {self.name} - Status: {self.status}"
    
    class Meta:
        db_table = 'drone'

class Mission(models.Model):
    STATUS_CHOICES = [
        ("planned", "Planned"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("aborted", "Aborted"),
        ("paused", "Paused"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="planned")
    survey_area = models.JSONField()
    altitude = models.FloatField()
    distance_covered = models.FloatField(default=0)
    progress = models.IntegerField(default=0)
    estimated_time_remaining = models.IntegerField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    flight_path = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Mission {self.id} for Drone {self.drone.name} - Status: {self.status}"
    
    class Meta:
        db_table = 'mission'
