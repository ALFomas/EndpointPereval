from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Camping
from .serializers import CampingSerializer


class SubmitData(APIView):
    """Сlass that processes POST type requests"""

    def post(self, request):
        """Method for post data"""
        data = request.data
        camping_serializer = CampingSerializer(data=data)

        if camping_serializer.is_valid():
            camping = camping_serializer.save()
            camping.submit_to_db()

            return Response(camping_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(camping_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CampingDetailView(APIView):
    """Сlass that show camping details"""

    def get(self, request, id):
        """pass"""
        camping = Camping.objects.filter(id=id).first()
        if camping:
            serializer = CampingSerializer(camping)
            return Response(serializer.data)
        else:
            return Response({"error": "Camping not found"}, status=status.HTTP_404_NOT_FOUND)
