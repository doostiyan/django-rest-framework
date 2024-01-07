from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from home.models import Person
from home.serializers import PersonSerializer


class Home(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerializer(instance=persons, many=True)
        return Response({'name': 'jack'})

