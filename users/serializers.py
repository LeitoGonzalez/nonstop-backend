from rest_framework import serializers
from .models import Result

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['id', 'user', 'wpm', 'accuracy', 'errors', 'score', 'date']
        read_only_fields = ['id', 'user', 'date']