from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


# ==========================================
# Register Serializer
# ==========================================

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        min_length=6,
    )

    class Meta:
        model = User
        fields = (
            "full_name",
            "email",
            "phone",
            "password",
        )

        extra_kwargs = {
            "email": {
                "required": True,
            },
            "phone": {
                "required": False,
                "allow_blank": True,
            },
        }

    def validate_email(self, value):

        if User.objects.filter(email=value).exists():

            raise serializers.ValidationError(
                "Email already exists."
            )

        return value

    def create(self, validated_data):

        return User.objects.create_user(

            email=validated_data["email"],

            full_name=validated_data["full_name"],

            password=validated_data["password"],

            phone=validated_data.get(
                "phone",
                "",
            ),

        )


# ==========================================
# User Serializer
# ==========================================

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = (
            "id",
            "full_name",
            "email",
            "phone",
        )

        read_only_fields = (
            "id",
            "email",
        )


# ==========================================
# Profile Serializer
# ==========================================

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = (
            "id",
            "full_name",
            "email",
            "phone",
        )

        read_only_fields = (
            "id",
            "email",
        )


# ==========================================
# Change Password Serializer
# ==========================================

class ChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField(
        required=True,
        write_only=True,
    )

    new_password = serializers.CharField(
        required=True,
        min_length=6,
        write_only=True,
    )

    confirm_password = serializers.CharField(
        required=True,
        write_only=True,
    )

    def validate(self, attrs):

        if (
            attrs["new_password"]
            != attrs["confirm_password"]
        ):

            raise serializers.ValidationError(
                {
                    "confirm_password":
                    "Passwords do not match."
                }
            )

        return attrs