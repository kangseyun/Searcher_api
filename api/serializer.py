from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from api.models import Issue, Communite, ConditionExpressList, InvestmentItems

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
    subject = serializers.CharField(required=False, allow_blank=True, max_length=100)
    content = serializers.CharField(max_length=65535)
    user_name = serializers.CharField(max_length=64)
    created = serializers.DateTimeField()

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

    class Meta:
        model = Communite
        fields = ('content', 'user_name', 'user_email', 'created')

class communityJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None, status=False):
        if status == True:
            data['status'] = "self"

        return super(communityJSONRenderer, self).render(data, accepted_media_type, renderer_context)

class ConditionSerializer(serializers.Serializer):
    express_index = serializers.IntegerField()
    express_name = serializers.CharField(max_length=64)

    class Meta:
        model = ConditionExpressList

class ConditionItemSerializer(serializers.Serializer):
    item_name = serializers.CharField(max_length=48)

    class Meta:
        model = InvestmentItems