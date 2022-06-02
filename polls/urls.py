from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name = 'index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name = 'detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/result/', views.results, name = 'result'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name = 'votes'),
    ]
