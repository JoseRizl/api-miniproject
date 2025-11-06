from django.urls import path, include
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter
from api.views import student_function_base_view
from api.views import employee_function_base_view
from api.views import student_class_base_view
from api.views import employee_class_base_view
from api.views import mixins_employee
from api.views import mixins_student
from api.views import generics_employee
import api.views.employee_viewsets as employee_viewsets_view
import api.views.student_viewsets as student_viewsets_view
from api.views import nested_serializer_view


router = DefaultRouter()
router.register('viewsets-employees', employee_viewsets_view.Employees, basename='viewsets-employees'),
router.register('model-viewsets-employees', employee_viewsets_view.EmployeeModelViewSet),
router.register('viewsets-students', student_viewsets_view.Students, basename='viewsets-students'),
router.register('model-viewsets-students', student_viewsets_view.StudentModelViewSet),

urlpatterns = [
    path('fbv-students/', student_function_base_view.studentView),
    path('fbv-student/<int:pk>', student_function_base_view.student),

    path('fbv-employees/', employee_function_base_view.employeeView),
    path('fbv-employee/<int:pk>', employee_function_base_view.employee),

    path('cbv-students/', student_class_base_view.Students.as_view()),
    path('cbv-student/<int:pk>', student_class_base_view.StudentDetail.as_view()),

    path('cbv-employees/', employee_class_base_view.Employees.as_view()),
    path('cbv-employee/<int:pk>', employee_class_base_view.EmployeeDetail.as_view()),

    path('mixins-employees/', mixins_employee.Employees.as_view()), 
    path('mixins-employee-detail/<int:pk>', mixins_employee.EmployeeDetail.as_view()), 

    path('mixins-students/', mixins_student.Students.as_view()), 
    path('mixins-student-detail/<int:pk>', mixins_student.StudentDetail.as_view()), 

    path('generics-employees/', generics_employee.Employees.as_view()), 
    path('generics-employee-detail/<int:pk>', generics_employee.EmployeeDetail.as_view()),

    path('', include(router.urls)),

    path('blogs/', nested_serializer_view.BlogsView.as_view()),
    path('comments/', nested_serializer_view.CommentsView.as_view()),

    path('blogs/<int:pk>', nested_serializer_view.BlogDetailView.as_view()),
    path('comments/<int:pk>', nested_serializer_view.CommentDetailView.as_view()),

]