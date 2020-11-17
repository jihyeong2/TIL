from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer

# Create your views here.

@api_view(['POST'])
def signup(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user=serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data)
