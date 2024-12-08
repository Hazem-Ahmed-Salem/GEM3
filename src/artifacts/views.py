from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *


@api_view(['GET'])
def all_art(request,lang):
    art = Artifact.objects.all()
    if not art:
        return Response("Nothing Found!!",status=status.HTTP_404_NOT_FOUND)
    if lang == 'en':
        serialized = ENArtSerializer(art,many=True)
    elif lang == 'gr':
        serialized = GRArtSerializer(art,many=True)
    elif lang == 'rus':
        serialized = RUSArtSerializer(art,many=True)
    elif lang == 'ar':
        serialized = ARArtSerializer(art,many=True)
    else:
        return Response("Language Format in Route is Wrong ",status=status.HTTP_400_BAD_REQUEST)
    return Response(serialized.data)

@api_view(["GET"])
def one_art(request,id,lang):
    art = Artifact.objects.filter(id=id)
    if not art:
        return Response("Nothing Found!!",status=status.HTTP_404_NOT_FOUND)
    if lang == 'en':
        serialized = ENArtSerializer(art,many=False)
    elif lang == 'gr':
        serialized = GRArtSerializer(art,many=False)
    elif lang == 'rus':
        serialized = RUSArtSerializer(art,many=False)
    elif lang == 'ar':
        serialized = ARArtSerializer(art,many=True)
    else:
        return Response("Language Format in Route is Wrong ",status=status.HTTP_400_BAD_REQUEST)
    return Response(serialized.data)


@api_view(["POST"])
def add_art(request):
    art = ArtSerializer(request.POST,request.FILES)
    art.is_valid(raise_exception=True)
    art.create(art.validated_data)
    return Response({"message":"it was created successfully",
                     "artifact":art._data},status=status.HTTP_200_OK)