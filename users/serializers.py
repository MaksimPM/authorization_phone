from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    otp_code = serializers.CharField(required=False)
    invite_code = serializers.CharField(required=False)
    activated_user_phone_numbers = serializers.ListField(child=serializers.CharField(), read_only=True)

    class Meta:
        model = User
        fields = ['phone_number', 'otp_code', 'invite_code', 'other_profile_invite_code',
                  'activated_user_phone_numbers']