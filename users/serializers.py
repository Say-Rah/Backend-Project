from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)  # Confirm password field
    is_admin = serializers.BooleanField(default=False)  # Add is_admin field

    class Meta:
        model = CustomUser
        fields = ('email','username', 'first_name', 'last_name', 'password', 'password2', 'is_admin')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords must match."})

        # Validate password strength
        validate_password(data['password'])
        return data

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_admin=validated_data.get('is_admin', False)  # Set the is_admin field
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
from rest_framework import serializers

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        fields = ['email', 'password']
