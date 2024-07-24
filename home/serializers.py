from rest_framework import serializers

from home.custom_realational_fields import UserEmailRelationalField
from home.models import Question, Answer, Person


class PersonSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()
    # class Meta:
    #     model = Person
    #     fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    answer = serializers.SerializerMethodField()
    user = UserEmailRelationalField(read_only=True) # serializer relations
    # user = serializers.StringRelatedField(read_only=True)   # username نشان میده
    # user = serializers.PrimaryKeyRelatedField(read_only=True)
    # user = serializers.SlugRelatedField(read_only=True, slug_field='email')
    class Meta:
        model = Question
        fields = '__all__'

    def get_answer(self, obj):   # miscellaneous-field # obj همون سوالات است
        result = obj.answers.all() # تمام پاسخ هایی که مربوط به این سوالات است می گیریم
        return AnswerSerializer(instance=result, many=True).data


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

