from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404 
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import Http404 
from rest_framework import status
from .paginations import UserPagination 
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import SignUpSerializer ,CreateUserSerializer,RetrievalUserSerializer
from pprint import pprint


class Users(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        users = User.objects.all()
        serialized = RetrievalUserSerializer(users,many=True)
        return Response(serialized.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def sign_up(request):
    user = SignUpSerializer(data=request.data)
    try:
        user.is_valid(raise_exception=True)
        user.create(user.validated_data)
        query = User.objects.get(username=user.data['username'])
        pprint(query)
        refresh = RefreshToken.for_user(query)
        return Response({
            "refresh":str(refresh),
            "access":str(refresh.access_token)
        })
    except Exception as e:
        pprint(e)
        return Response({"message":"there is something wrong with your data"})


class UsersView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        pprint(request)
        users = User.objects.all()
        serialized = RetrievalUserSerializer(users,many=True)
        return Response(serialized.data)
    
    def post(self,request):
        pprint(request)
        user = User.objects.create(data=request.data)
        serialized = CreateUserSerializer(user)
        return Response(serialized.data)
    




# @api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
# def users(request):
#     pprint(request)
#     if request.method == 'GET':
#         users = User.objects.all()
#         serialized = RetrievalUserSerializer(users,many=True)
#         return Response(serialized.data,status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         user = User.objects.create(data=request.data)
#         serialized = CreateUserSerializer(user)
        
#         return Response(serialized.data)

@api_view(['GET','DELETE'])
@permission_classes([IsAuthenticated])
def user(request,id):
    try:
        user = get_object_or_404(User,id=id)
        serialized = RetrievalUserSerializer(user,many=False)
    except Http404:
        return Response({"message":"the user wasn't found",
                         "failed":True})
    
    if request.method == "GET":
        return Response(serialized.data,status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        try:
            user.delete()
            return Response({"message":"the user was delete successfully deleted",
                            "deleted":True},status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            Response({"message":f"{e}",
                      "deleted":False},status=status.HTTP_400_BAD_REQUEST)



 

