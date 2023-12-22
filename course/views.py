from django.http.response import HttpResponse, JsonResponse
from .models import Course, Main_Learn, Sub_Learn, Sub_Sub_Learn, Teacher
from django.shortcuts import render


def course_list(request):
    #  this is view for list of courses
    course = Course.objects.all()
    courses = {
        'courses' : course
    }
    return render(request, 'main_page/main_page.html', context=courses)

def course_page(request):
    #  this is a view for course detail
    course = Course.objects.all()
    courses = {
        'courses' : course
    }
    return render(request, 'course_page/course_page.html', context=courses)


def teachers_page(request):
    #  this is a view for teacher list
    teacher = Teacher.objects.all()
    teachers = {
        'Teachers' : teacher
    }
    return render(request, 'teachers_list/teachers_list.html', context=teachers)

