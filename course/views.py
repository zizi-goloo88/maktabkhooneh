from django.http.response import HttpResponse, JsonResponse
from .models import Course, Main_Learn, Sub_Learn, Sub_Sub_Learn, Teacher,Ticket
from django.shortcuts import render
from random import randint


def course_list(request):
    course = Course.objects.all()
    courses = {
        'courses' : course
    }
    return render(request, 'main_page/main_page.html', context=courses)



def teachers_page(request):
    teacher = Teacher.objects.all()
    teachers = {
        'Teachers' : teacher
    }
    return render(request, 'teachers_list/teachers_list.html', context=teachers)

def course_page(request, code):
    if request.method == 'GET':
            try:
                course = Course.objects.get(number=code)
            except:
                course = None
            courses = {
                'courses' : course
            }
            return render(request, 'course_page/course_page.html', context=courses)
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        lastname = request.POST['lastname']
        nationalid = request.POST['nationalid']
        seat = request.POST['seat']
        Ticket.objects.create(
            #  course= Sub_Sub_Learn.objects.get(number=code),
             email=email,
             name=name,
             last_name=lastname,
             nationalid=nationalid,
             seat=seat,
             reservation= generate_random_code()
            )
        return HttpResponse('The ticket reserved!')

def generate_random_code():
    code = randint(10000000,99999999)
    try:
        Ticket.objects.get(reservation=code)
        generate_random_code()
    except:
        return code
