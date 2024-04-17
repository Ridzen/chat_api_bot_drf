from rest_framework import serializers


class ChatRequestSerializer(serializers.Serializer):
    prompt = serializers.CharField()


class ChatResponseSerializer(serializers.Serializer):
    response = serializers.CharField()
