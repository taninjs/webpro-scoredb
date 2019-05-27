from django.db import models


# Create your models here.
from django.db.models import Sum


class Student(models.Model):
    student_id = models.CharField(max_length=10)

    def __str__(self):
        return self.student_id

    def has_conflict(self):
        fscore_set = self.frontendscore_set.all().order_by('question')
        bscore_set = self.backendscore_set.all().order_by('question')

        if fscore_set.count() != bscore_set.count():
            return True

        for fscore, bscore in zip(fscore_set, bscore_set):
            if fscore.score != bscore.score:
                return True

        return False

    def total_frontend_score(self):
        return self.frontendscore_set.aggregate(Sum('score'))['score__sum']

    def total_backend_score(self):
        return self.backendscore_set.aggregate(Sum('score'))['score__sum']


class FrontendScore(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.CharField(max_length=10)
    score = models.DecimalField(max_digits=4, decimal_places=2)
    comment = models.TextField()

    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.timestamp)


class BackendScore(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.CharField(max_length=10)
    score = models.DecimalField(max_digits=4, decimal_places=2)
    comment = models.TextField()

    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.timestamp)

