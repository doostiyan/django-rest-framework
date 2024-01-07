from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()
