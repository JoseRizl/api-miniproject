
from django.urls import path
from api.views import student_function_base_view
from api.views import employee_function_base_view
from api.views import student_class_base_view

urlpatterns = [
    path('fbv-students/', student_function_base_view.studentView),
    path('fbv-students/<int:pk>', student_function_base_view.student),

    path('fbv-employees/', employee_function_base_view.employeeView),
    path('fbv-employees/<int:pk>', employee_function_base_view.employee),

    path('cbv-students/', student_class_base_view.Students.as_view()),
]