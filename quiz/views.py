from django.shortcuts import render, redirect
from .models import Question, UserQuizSession
import random

def start_quiz(request):
    session = UserQuizSession.objects.create()
    request.session['session_id'] = session.id
    return redirect('get_question')

def get_question(request):
    session_id = request.session.get('session_id')
    if not session_id:
        return redirect('start_quiz')

    question = Question.objects.first()
    return render(request, 'quiz/question.html', {'question': question})


def submit_answer(request):
    if request.method == 'POST':
        session_id = request.session.get('session_id')
        if not session_id:
            return redirect('start_quiz')

        session = UserQuizSession.objects.get(id=session_id)
        question_id = request.POST.get('question_id')
        selected_option = request.POST.get('selected_option')
        question = Question.objects.get(id=question_id)

        session.total_questions += 1
        if question.correct_option == selected_option:
            session.correct_answers += 1
        else:
            session.incorrect_answers += 1
        session.save()

        return redirect('get_question')

def get_results(request):
    session_id = request.session.get('session_id')
    if not session_id:
        return redirect('start_quiz')

    session = UserQuizSession.objects.get(id=session_id)
    return render(request, 'results.html', {
        'total_questions': session.total_questions,
        'correct_answers': session.correct_answers,
        'incorrect_answers': session.incorrect_answers,
    })
