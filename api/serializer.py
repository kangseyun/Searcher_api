from rest_framework import serializers
from api.models import Issue, LANGUAGE_CHOICES, STYLE_CHOICES, Communite

class IssueSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    subject = serializers.CharField(required=False, allow_blank=True, max_length=100)
    content = serializers.CharField(style={'base_template': 'textarea.html'})
   

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.subject = validated_data.get('subject', instance.title)
        instance.content = validated_data.get('content', instance.code)

        instance.save()
        return instance

class communitySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    subject = serializers.CharField(required=False, allow_blank=True, max_length=100)
    content = serializers.CharField(style={'base_template': 'textarea.html'})
   

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.subject = validated_data.get('subject', instance.title)
        instance.content = validated_data.get('content', instance.code)

        instance.save()
        return instance