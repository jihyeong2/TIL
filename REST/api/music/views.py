from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Artist,Music
from .serializers import (
    ArtistListSerializer,ArtistSerializer,
    MusicListSerializer,MusicSerializer)

# Create your views here.

@api_view(['GET','POST'])
def artist_list_create(request):
    if request.method=='GET':
        artists=Artist.objects.all()
        serializer=ArtistListSerializer(artists,many=True)
        return Response(serializer.data)
    else:
        serializer=ArtistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def artist_detail(request,artist_pk):
    artist=get_object_or_404(Artist,pk=artist_pk)
    serializer=ArtistSerializer(artist)
    return Response(serializer.data)


@api_view(['POST'])
def artist_music(request,artist_pk):
    artist=get_object_or_404(Artist,pk=artist_pk)
    serializer=MusicSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(artist=artist)
        return Response(serializer.data)


@api_view(['GET'])
def music(request):
    musics=Music.objects.all()
    serializer=MusicListSerializer(musics,many=True)
    return Response(serializer.data)


@api_view(['GET','PUT','DELETE'])
def music_detail_update_delete(request,music_pk):
    music=get_object_or_404(Music,pk=music_pk)
    if request.method=='GET':
        serializer=MusicSerializer(music)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=MusicSerializer(music,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        music.delete()
        return Response({'id':music_pk})