from django.urls import path

from . import views


urlpatterns = [
    path('create/frontend/', views.FrontendScoreCreateAPI.as_view()),
    path('create/backend/', views.BackendScoreCreateAPI.as_view()),

    path('report/', views.ScoreExportCSV.as_view())
]