from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HealthView(APIView):
    """
    A simple test view to verify that the API is working.
    """
    
    def get(self, request):
        """
        Handle GET requests to the test endpoint.
        """
        return Response({"message": "Health is good"}, status=status.HTTP_200_OK)
    