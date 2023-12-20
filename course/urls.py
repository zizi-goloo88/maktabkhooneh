from django.urls import path
from .views import course_list, course_page
urlpatterns = [
    path('', course_list, name='course_list'),
    path('course', course_page, name='course_page'),
    
]