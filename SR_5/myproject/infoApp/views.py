from django.shortcuts import render

from django.http import HttpResponse


def student_info(request):

    text_content = """Інформація про студента
Прізвище Ім'я: Кішко Олексій
Группа: ІСД-32
"""

    return HttpResponse(text_content, content_type='text/plain; charset=utf-8')