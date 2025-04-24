from django.urls import path
from .views import employee_list, add_employee, edit_employee, delete_employee


urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('addemp/', add_employee, name='add_employee'),
    path('editemp/<int:id>/', edit_employee, name='edit_employee'),
    path('deleteemp/<int:id>/', delete_employee, name='delete_employee'),
]