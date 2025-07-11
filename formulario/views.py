from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages

from .models import Quiz, Pergunta, OpcaoResposta
from .forms import QuizForm

def quiz_home(request):
    quizzes = Quiz.objects.all()
    return render(request, 'formulario/quiz_home.html', {'quizzes': quizzes})

def criar_quiz(request):
    quiz = None

    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save()
            return redirect('criar_quiz_com_id', quiz_id=quiz.id)
    else:
        form = QuizForm()

    return render(request, 'formulario/criar_pergunta.html', {
        'form': form,
        'quiz': quiz,
    })

def criar_quiz_com_id(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    perguntas = quiz.perguntas.all()  # Obter perguntas já associadas ao quiz

    if request.method == 'POST':
        textos = request.POST.getlist('texto[]')
        tipos = request.POST.getlist('tipo[]')
        opcoes_inputs = request.POST.getlist('opcao[]')
        respostas_curtas = request.POST.getlist('resposta_curta[]')

        # Limpar perguntas existentes para evitar duplicação ao salvar
        Pergunta.objects.filter(quiz=quiz).delete()  # Remove todas as perguntas associadas ao quiz

        idx_opcao_global = 0  # Índice para percorrer todas as opções enviadas
        idx_resposta_curta_global = 0  # Índice para percorrer todas as respostas curtas enviadas

        for i in range(len(textos)):
            texto_pergunta = textos[i]
            tipo_pergunta = tipos[i]
            resposta_correta_pergunta = None  # Renomeado para resposta_correta

            if tipo_pergunta == 'curta':
                if idx_resposta_curta_global < len(respostas_curtas):
                    resposta_correta_pergunta = respostas_curtas[idx_resposta_curta_global]
                    idx_resposta_curta_global += 1
            
            # Cria a instância da Pergunta e associa ao quiz
            pergunta = Pergunta.objects.create(
                quiz=quiz,  # Associando a pergunta ao quiz
                texto=texto_pergunta,
                tipo=tipo_pergunta,
                resposta_correta=resposta_correta_pergunta  # Usando o novo nome do campo
            )

            if tipo_pergunta == 'multipla':
                # Coleta as opções para a pergunta atual
                current_pergunta_opcoes = []
                while idx_opcao_global < len(opcoes_inputs) and opcoes_inputs[idx_opcao_global].strip():
                    current_pergunta_opcoes.append(opcoes_inputs[idx_opcao_global].strip())
                    idx_opcao_global += 1
                
                for opcao_texto in current_pergunta_opcoes:
                    OpcaoResposta.objects.create(pergunta=pergunta, texto_opcao=opcao_texto)
                
                # Se houver um campo vazio que separa as opções de diferentes perguntas, consuma-o
                if idx_opcao_global < len(opcoes_inputs) and not opcoes_inputs[idx_opcao_global].strip():
                    idx_opcao_global += 1  # Consumir o separador vazio (se houver)

        messages.success(request, "Perguntas salvas com sucesso!")
        return redirect('criar_quiz_com_id', quiz_id=quiz.id)

    return render(request, 'formulario/criar_pergunta.html', {
        'quiz': quiz,
        'perguntas': perguntas,
    })


def finalizar_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == 'POST':
        if quiz.perguntas.count() == 0:  # Verifica as perguntas associadas via ManyToManyField
            messages.error(request, "Adicione pelo menos uma pergunta antes de finalizar.")
            return redirect('criar_quiz_com_id', quiz_id=quiz.id)
        return redirect('quiz_home')

def responder_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    perguntas = quiz.perguntas.all()  # Obter perguntas associadas via ManyToManyField
    return render(request, 'formulario/responder_quiz.html', {
        'quiz': quiz,
        'perguntas': perguntas
    })

def eliminar_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == 'POST':
        quiz.delete()
        return redirect('quiz_home')
    return render(request, 'template/formulario/eliminar_quiz.html', {'quiz': quiz})

def verificar_respostas(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    perguntas = quiz.perguntas.all() 
    respostas = request.POST  #Mostrar as respostas do formulário
    # Lógica para verificar as respostas
    return render(request, 'formulario/resultados.html', {
        'quiz': quiz,
        'perguntas': perguntas,
        'respostas': respostas,
    })
