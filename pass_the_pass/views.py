from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Camping
from .serializers import CampingSerializer, CampingPatchSerializer
from rest_framework import generics


class SubmitData(APIView):
    """View that processes POST type requests"""

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
    """View that show camping details"""

    def get(self, request, id):
        """Method for get and show data"""
        camping = Camping.objects.filter(id=id).first()
        if camping:
            serializer = CampingSerializer(camping)
            return Response(serializer.data)
        else:
            return Response({"error": "Camping not found"}, status=status.HTTP_404_NOT_FOUND)


class CampingPatchView(generics.UpdateAPIView):
    """ View that edit some camping's fields"""
    queryset = Camping.objects.filter(status='NW')  # Фильтрация записей по статусу "New"
    serializer_class = CampingPatchSerializer

    def update(self, request, *args, **kwargs):
        """Method for path some fields"""
        instance = self.get_object()
        if instance.status != 'NW':  # Проверка статуса записи
            return Response({"state": 0, "message": "Record status is not 'New'"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({"state": 1}, status=status.HTTP_200_OK)
