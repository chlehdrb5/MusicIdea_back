from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User
from user.serializer import UserSignupSerializer


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save(request)
        token = RefreshToken.for_user(user)
        refresh = str(token)
        access = str(token.access_token)

        return Response({
            'user': user.name,
            'access': access,
            'refresh': refresh
        })
