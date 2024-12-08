# serializers.py
from rest_framework import serializers
from .models import Artifact

class ArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = ['name', 'audio_fileEN','audio_fileEN','audio_fileGR','audio_fileRUS','audio_fileAR',
                  'descriptionEN','descriptionGR','descriptionRUS','descriptionAR']
        
        def create(self, validated_data):
        # You can add custom logic here if needed, such as processing the file before saving
            return Artifact.objects.create(**validated_data)


class ENArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = ['id', 'name', 'audio_fileEN', 'descriptionEN', 'created_at']

class GRArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = ['id', 'name', 'audio_fileGR', 'descriptionGR', 'created_at']

class RUSArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = ['id', 'name', 'audio_fileRUS', 'descriptionRUS', 'created_at']

class ARArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = ['id', 'name', 'audio_fileAR', 'descriptionAR', 'created_at']
