from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=80)
    email = serializers.EmailField(max_length=100)
