from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.
# 인증 : 클라이언트가 누구인지를 서버에서 아는 것
# 세션기반인증 : 로그인을 하면 서버에서 로그인정보로 랜덤한 세션아이디를 만들어 서버에 저장.
# 클라이언트에 세션아이디를 준다.

# 토큰기반인증 : 유저가 누구인지를 써서 만든 토큰을 준다.
# 서명(서버만 알고 있는 비밀키)
# 유저가 갖고 있는 토큰을 인증서처럼 사용한다.

# 차이 : 세션은 서버가 세션을 갖고 있어야 하지만, 토큰 인증방식은
# 유저가 갖고 있는 토큰만 해독하면 되기 때문에 중앙관리시스템이 필요하지 않다.
# 하지만 토큰은 수명이 있고, 수명이 짧으면 계속 재로그인이 필요하다. 수명이 길면
# 해킹의 위험이 있다.
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication]) #도착한 토큰이 정상적인지 검사
# 토큰이 정상적이라면 request에 user객체를 담아준다.
@permission_classes([IsAuthenticated]) # 토근이 담겨있는지 아닌지 검사
def todo_list_create(request):
    if request.method == 'GET':
        # todo database에서 todo 정보를 모두 긁어서 JSON응답
        # model => QuerySet => dict, string => JSON응답
        todos = Todo.objects.all()
        serializer = TodoSerializer(request.user.todos, many=True)
        return Response(serializer.data)
    else:
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)


@api_view(['PUT','DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def todo_update_delete(request,id):
    todo=get_object_or_404(Todo,pk=id)
    if request.method=='PUT':
        serializer=TodoSerializer(instance=todo,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


    else:
        todo.delete()
        return Response({'id':id})

