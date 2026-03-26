# # views.py
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Product
# from .serializers import ProductSerializer


# @api_view(["GET"])
# def get_products(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True,context={'request': request})
#     return Response(serializer.data)


# @api_view(["POST"])
# def upload_product(request):
#     serializer = ProductSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)

#     return Response(serializer.errors)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer

@api_view(['POST'])
def upload_product(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            "status": True,
            "message": "Image and Audio uploaded successfully",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    return Response({
        "status": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_products(request):
    data = Product.objects.all()
    serializer = ProductSerializer(data, many=True, context={'request': request})
    return Response({
        "status": True,
        "data": serializer.data
    })