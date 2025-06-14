from api.models import Mission, Drone
from django.utils import timezone
import random

def start_missions():
    starting_missions = Mission.objects.filter(status='planned')

    for mission in starting_missions:
        drone = mission.drone

        # Simulate transition to in_progress
        mission.status = 'in_progress'
        mission.start_time = mission.start_time or timezone.now()
        mission.save()

        # Update drone status as well
        drone.status = 'in_mission'
        drone.save()

        print(f"Mission {mission.id} started for Drone {drone.id}")

def simulate_mission_progress():
    missions = Mission.objects.filter(status='in_progress')

    for mission in missions:
        # Progress update logic: +34 per cron, after 3 updates reaches ~100
        mission.progress += 100
        drone = mission.drone

        if mission.progress >= 100:
            mission.progress = 100
            mission.status = 'completed'
            mission.end_time = timezone.now()
            mission.distance_covered = random.randint(300, 1000)  # meters

            drone.status = 'available'
            drone.save()

        mission.save()