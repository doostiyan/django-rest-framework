from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import UserRegisterSerializer


class UserRegister(APIView):

    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = [IsAuthenticated]

    def list(self, request):
        srz_data = UserRegisterSerializer(instance=self.queryset, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        srz_data = UserRegisterSerializer(instance=user)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        if user != request.user:
            return Response({'permission_denied': 'You are not owner'})
        srz_data = UserRegisterSerializer(instance=user, data=request.POST, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data)
        return Response(srz_data.errors)

    def destroy(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        if user != request.user:
            return Response({'permission_denied': 'You are not owner'})
        user.is_active = False
        user.save()
        return Response({'message': 'User has been deactivated'})