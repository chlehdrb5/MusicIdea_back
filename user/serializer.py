from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User


class UserSignupSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20, required=True, write_only=True)
    password = serializers.CharField(style={'input_type': 'password'}, required=True, write_only=True)

    class Meta:
        model = User
        fields = ['name', 'password', 'profile_img']

    def save(self, request):
        user = super().save()

        user.name = self.validated_data['name']
        user.set_password(self.validated_data['password'])
        if 'profile_img' in self.validated_data:
            user.profile_img = self.validated_data['profile_img']
        user.save()

        return user

    def validate(self, data):
        name = data.get('name', None)
        if User.objects.filter(name=name).exists():
            raise serializers.ValidationError("user already exists")

        return data
