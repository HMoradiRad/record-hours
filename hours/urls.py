from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_works, name='all_works'),
    path('add-new-task/', views.task_new_add, name="add_new_task"),
]