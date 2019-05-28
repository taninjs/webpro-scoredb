from rest_framework import serializers
from .models import BackendScore, FrontendScore, Student


class BackendScoreSerializer(serializers.ModelSerializer):
    student = serializers.CharField(source='student.student_id')

    class Meta:
        model = BackendScore
        fields = ('id', 'student', 'question', 'score', 'comment')

    def create(self, validated_data):
        student, is_created = Student.objects.get_or_create(student_id=validated_data['student']['student_id'])

        score, is_created = BackendScore.objects.get_or_create(
            student=student,
            question=validated_data['question'],
            defaults={
                'score': validated_data['score'],
                'comment': validated_data['comment']
            }
        )

        if not is_created:
            score.score = validated_data['score']
            score.comment = validated_data['comment']
            score.save()

        return score


class FrontendScoreSerializer(serializers.ModelSerializer):
    student = serializers.CharField(source='student.student_id')

    class Meta:
        model = FrontendScore
        fields = ('id', 'student', 'question', 'score', 'comment')

    def create(self, validated_data):
        student, is_created = Student.objects.get_or_create(student_id=validated_data['student']['student_id'])

        score, is_created = FrontendScore.objects.get_or_create(
            student=student,
            question=validated_data['question'],
            defaults={
                'score': validated_data['score'],
                'comment': validated_data['comment']
            }
        )

        if not is_created:
            score.score = validated_data['score']
            score.comment = validated_data['comment']
            score.save()

        return score
