from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Bestsellings
from .serializers import bestsellingsSerializer

@api_view(['POST'])
def upload_Best(request):
    serializer = bestsellingsSerializer(data=request.data)

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
def get_Best(request):
    data = Bestsellings.objects.all()
    serializer = bestsellingsSerializer(data, many=True, context={'request': request})
    return Response({
        "status": True,
        "data": serializer.data
    })