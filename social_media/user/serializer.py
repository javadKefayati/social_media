from rest_framework import serializers
from django.contrib.auth import get_user_model
from .validators import number_validator, special_char_validator, letter_validator
from django.core.validators import MinLengthValidator


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
            validators=[
                    number_validator,
                    letter_validator,
                    special_char_validator,
                    MinLengthValidator(limit_value=10)
                ],
                write_only=True,
            )
    confirm_password = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = get_user_model() 
        fields = ("username","password","confirm_password","email","is_admin","is_superuser","created_at")
        extra_kwargs = {
            'is_admin': {'read_only': True},
            'is_superuser': {'read_only': True},
            'created_at': {'read_only': True},
        }

        def validate_email(self, email):
            if get_user_model().objects.filter(email=email).exists():
                raise serializers.ValidationError("email Already Taken")
            return email

        def validate(self, data):
            if not data.get("password") or not data.get("confirm_password"):
                raise serializers.ValidationError("Please fill password and confirm password")
            
            if data.get("password") != data.get("confirm_password"):
                raise serializers.ValidationError("confirm password is not equal to password")
            return data
