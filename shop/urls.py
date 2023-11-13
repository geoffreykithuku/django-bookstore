from django.urls import path

from shop import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:course_id>', views.show, name='show')
]
