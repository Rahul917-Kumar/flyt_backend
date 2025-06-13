# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Drone
from api.serializers.drone_serializer import DroneSerializer
from django.shortcuts import get_object_or_404

class DroneListCreateAPIView(APIView):
    def get(self, request):
        drones = Drone.objects.all()
        serializer = DroneSerializer(drones, many=True)
        return Response({"message":"Successfully fetched all drones", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DroneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Drone created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to create drone", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class DroneDetailAPIView(APIView):
    def get(self, request, pk):
        drone = get_object_or_404(Drone, pk=pk)
        serializer = DroneSerializer(drone)
        return Response({"message": "Drone details fetched successfully", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        drone = get_object_or_404(Drone, pk=pk)
        serializer = DroneSerializer(drone, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Drone updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"message": "Failed to update drone", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
