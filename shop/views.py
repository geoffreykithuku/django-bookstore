from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import http

from shop.models import Course


# Create your views here.
def index(request):
    data = Course.objects.all()
    return render(request, 'courses.html', {"courses": data})


def show(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'show.html', {"course": course})