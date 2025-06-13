
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Mission
from api.serializers.mission_serializer import MissionSerializer
from django.shortcuts import get_object_or_404
from django.utils import timezone

class MissionListCreateAPIView(APIView):
    def get(self, request):
        missions = Mission.objects.all()
        serializer = MissionSerializer(missions, many=True)
        return Response({"message": "Successfully fetched all missions", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Mission created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to create mission", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class MissionDetailAPIView(APIView):
    def get(self, request, pk):
        mission = get_object_or_404(Mission, pk=pk)
        serializer = MissionSerializer(mission)
        return Response(serializer.data)

    def patch(self, request, pk):
        mission = get_object_or_404(Mission, pk=pk)
        serializer = MissionSerializer(mission, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Mission updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"message": "Failed to update mission", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class PauseMissionAPIView(APIView):
    def post(self, request, pk):
        mission = get_object_or_404(Mission, pk=pk)
        if mission.status == "in_progress":
            mission.status = "paused"
            mission.save()
            return Response({"message": "Mission paused."}, status=status.HTTP_200_OK)
        return Response({"message": "Mission not in progress."}, status=status.HTTP_400_BAD_REQUEST)

class ResumeMissionAPIView(APIView):
    def post(self, request, pk):
        mission = get_object_or_404(Mission, pk=pk)
        if mission.status == "paused":
            mission.status = "in_progress"
            mission.save()
            return Response({"message": "Mission resumed."}, status=status.HTTP_200_OK)
        return Response({"message": "Mission is not paused."}, status=status.HTTP_400_BAD_REQUEST)

class AbortMissionAPIView(APIView):
    def post(self, request, pk):
        mission = get_object_or_404(Mission, pk=pk)
        if mission.status in ["in_progress", "paused"]:
            mission.status = "aborted"
            mission.end_time = timezone.now()
            mission.save()
            return Response({"message": "Mission aborted."}, status=status.HTTP_200_OK)
        return Response({"message": "Cannot abort in current state."}, status=status.HTTP_400_BAD_REQUEST)
