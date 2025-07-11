from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_home, name='quiz_home'),  # Página inicial que lista quizzes
    path('criar/', views.criar_quiz, name='criar_quiz'),  # Criar quiz (passo inicial)
    path('criar/<int:quiz_id>/', views.criar_quiz_com_id, name='criar_quiz_com_id'),  # Adicionar perguntas
    path('quiz/<int:quiz_id>/responder/', views.responder_quiz, name='responder_quiz'),  # Responder quiz
    path('quiz/<int:quiz_id>/finalizar/', views.finalizar_quiz, name='finalizar_quiz'),  # Finalizar quiz
    path('eliminar/<int:quiz_id>/eliminar/', views.eliminar_quiz, name='eliminar_quiz'),  # Eliminar quiz
    path('verificar_respostas/<int:quiz_id>/', views.verificar_respostas, name='verificar_respostas'),
]
