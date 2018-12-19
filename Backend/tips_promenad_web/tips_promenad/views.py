from django.shortcuts import get_object_or_404
from tips_promenad.serializers import QuizPointSerializer
from tips_promenad.models import QuizPoint, Quiz
from rest_framework import viewsets
from rest_framework.response import Response

class QuizPointViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = QuizPoint.objects.all()
        serializer = QuizPointSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = QuizPoint.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = QuizPointSerializer(user)
        return Response(serializer.data)