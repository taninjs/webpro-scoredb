import csv

from django.http import HttpResponse
from django.views import View
from rest_framework.generics import CreateAPIView

from .models import BackendScore, Student
from .serializers import FrontendScoreSerializer, BackendScoreSerializer


class FrontendScoreCreateAPI(CreateAPIView):
    serializer_class = FrontendScoreSerializer


class BackendScoreCreateAPI(CreateAPIView):
    serializer_class = BackendScoreSerializer


class ScoreExportCSV(View):
    def get(self, request):
        filename = request.GET.get('filename', 'export.csv')

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        writer = csv.writer(response)
        questions = BackendScore.objects.all().values_list('question', flat=True).order_by('question').distinct()
        students = Student.objects.prefetch_related('backendscore_set', 'frontendscore_set').all()

        writer.writerow(['student_id'] + [x for x in questions] + ['total'])

        for student in students:
            bscores = []
            bscore_queryset = student.backendscore_set.order_by('question').values('question', 'score')

            for question in questions:
                bscores.append(next((x['score'] for x in bscore_queryset if x['question'] == question), '-'))

            fscores = []
            fscore_queryset = student.frontendscore_set.order_by('question').values('question', 'score')

            for question in questions:
                fscores.append(next((x['score'] for x in fscore_queryset if x['question'] == question), '-'))

            writer.writerow([student.student_id + ' (b)'] + bscores)
            writer.writerow([student.student_id + ' (f)'] + fscores)
        return response
