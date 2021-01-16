from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('work/<int:pk>/', views.work, name='work'),
    path('add-new-task/', views.add_new_task, name="add_new_task"),
    path('end-task/', views.end_task, name="end_task"),
    path('add-new-package/', views.task_new_package, name="add_new_package"),
]
