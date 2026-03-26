from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import newArrivals
from .serializer import ArrivalsSerializer

@api_view(['POST'])
def upload_arrivals(request):
    serializer = ArrivalsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            "status": True,
            "message": "Image uploaded successfully",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    return Response({
        "status": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_arrivals(request):
    data = newArrivals.objects.all()
    serializer = ArrivalsSerializer(data, many=True, context={'request': request})
    return Response({
        "status": True,
        "data": serializer.data
    })