from django.contrib import admin

from .models import FrontendScore, BackendScore, Student


@admin.register(FrontendScore)
class FrontendScoreAdmin(admin.ModelAdmin):
    list_display = ('student', 'question', 'score', 'comment', 'timestamp')
    list_filter = ('student', 'question')


@admin.register(BackendScore)
class BackendScoreAdmin(admin.ModelAdmin):
    list_display = ('student', 'question', 'score', 'comment', 'timestamp')
    list_filter = ('student', 'question')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    class FScoreInline(admin.TabularInline):
        model = FrontendScore
        extra = 0

        def get_queryset(self, request):
            return super().get_queryset(request).order_by('question')

    class BScoreInline(admin.TabularInline):
        model = BackendScore
        extra = 0

        def get_queryset(self, request):
            return super().get_queryset(request).order_by('question')

    change_list_template = 'scores_admin/students_changelist.html'

    list_display = ('student_id', 'has_conflict', 'total_frontend_score', 'total_backend_score')
    search_fields = ('student_id', )

    inlines = [FScoreInline, BScoreInline]
