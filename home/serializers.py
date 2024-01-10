from rest_framework import serializers

from home.custom_realational_fields import UserEmailRelationalField
from home.models import Question, Answer


class PersonSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()


class QuestionSerializer(serializers.ModelSerializer):
    answer = serializers.SerializerMethodField()
    user = UserEmailRelationalField(read_only=True)

    class Meta:
        model = Question
        fields = '__all__'

    def get_answer(self, obj):
        result = obj.answers.all()
        return AnswerSerializer(instance=result, many=True).data


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

