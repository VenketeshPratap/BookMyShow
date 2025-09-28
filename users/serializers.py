# users/serializers.py
from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'role']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        login_identifier = data.get('username') or data.get('email')
        password = data.get('password')
        if not login_identifier or not password:
            raise serializers.ValidationError('Username/email and password are required')

        # Try authenticate by username first; if email is provided, try that too
        user = None
        if data.get('username'):
            user = authenticate(username=data['username'], password=password)
        if user is None and data.get('email'):
            # Map email to username if the backend requires username
            try:
                candidate = User.objects.get(email=data['email'])
                user = authenticate(username=candidate.username, password=password)
            except User.DoesNotExist:
                user = None

        if not user:
            raise serializers.ValidationError('Invalid credentials')
        return user
