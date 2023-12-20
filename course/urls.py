from django.urls import path
from .views import course_list, course_page, teachers_page
urlpatterns = [
    path('', course_list, name='course_list'),
    path('course', course_page, name='course_page'),
    path('list', teachers_page, name='course_page'),

    
]