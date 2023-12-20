from django.http.response import HttpResponse, JsonResponse
from .models import Course, Main_Learn, Sub_Learn, Sub_Sub_Learn
from django.shortcuts import render


def course_list(request):
    course = Course.objects.all()
    courses = {
        'courses' : course
    }
    return render(request, 'main_page/main_page.html', context=courses)

def course_page(request):
    course = Course.objects.all()
    courses = {
        'courses' : course
    }
    return render(request, 'course_page/course_page.html', context=courses)

