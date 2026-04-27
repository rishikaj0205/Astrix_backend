from logging import exception

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from .models import Regform
from .serializer import RegformSerializer

@api_view(['GET'])
def get_logindetails(request):
    loginusers=Regform.objects.all()
    serializer=RegformSerializer(loginusers,many=True)
    return Response(serializer.data)


# @api_view(['GET'])
# def get_login(request):
#     user_id=request.GET.get('user_id')
#     loginusers=Student.objects.filter(user_id=user_id)
#     user_name=request.GET.get('user_name')
#     loginusers=Student.objects.filter(user_name=user_name)
#     serializer=StudentSerializer(loginusers,many=True)
#     return Response(serializer.data)

    

@api_view(['POST'])
def register_user(request):
    try:
        serializer = RegformSerializer(data=request.data)
        if serializer.is_valid():
            result= serializer.save()
            print("Res",result)
            return Response({"message": "Student registered successfully","data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": e}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def login_user(request):
#     email = request.data.get('email').strip()
#     password = request.data.get('password').strip()

#     try:
#         user = Regform.objects.get(email=email)    

#         if check_password(password, user.password):
#             return Response(({"message": "Login successful",'data': RegformSerializer(user).data}), status=status.HTTP_200_OK)
#         else:
#             return Response({"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)

#     except Regform.DoesNotExist:
#         return Response({"error": "user not found"}, status=status.HTTP_400_BAD_REQUEST)
#     except Exception as e:
#         return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        user = Regform.objects.get(email=email)

        if password == user.password:
            return Response({"message": "Login success"}, status=200)
        else:
            return Response({"error": "Invalid password"}, status=400)

    except Regform.DoesNotExist:
        return Response({"error": "User not found"}, status=400)