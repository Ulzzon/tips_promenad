from rest_framework import serializers
from tips_promenad.models import Quiz, QuizPoint

class QuizPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizPoint
        fields = ('id', 'question', 'right_answere', 'wrong_answere_1', 'wrong_answere_2', 'wrong_answere_3')