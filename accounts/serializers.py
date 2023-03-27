from django.contrib.auth import get_user_model
from rest_framework import serializers

from .validators import validate_email as email_is_valid

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "joind_at",
        ]


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "joind_at",
            "password",
        ]

    def validate_email(self, value):
        valid, error_text = email_is_valid(value)
        if not valid:
            raise serializers.ValidationError(error_text)
        try:
            email_name, domain_part = value.strip().rsplit("@", 1)
        except ValueError:
            pass
        else:
            value = "@".join([email_name, domain_part.lower()])
        return value


class UserUpadateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "joind_at",
        ]

    def validate_email(self, value):
        valid, error_text = email_is_valid(value)
        if not valid:
            raise serializers.ValidationError(error_text)
        try:
            email_name, domain_part = value.strip().rsplit("@", 1)
        except ValueError:
            pass
        else:
            value = "@".join([email_name, domain_part.lower()])
        return value
