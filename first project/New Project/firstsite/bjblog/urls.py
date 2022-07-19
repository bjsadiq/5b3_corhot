from django.urls import path  
from . import views

urlpatterns = [
    path("employees/", views.EmployeeListView(), name="employee_list"),
    
]
