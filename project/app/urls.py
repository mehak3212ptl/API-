from django.urls import path
from .views import *

urlpatterns = [
    path('stu_list/',stulist,name='stu'),
    path('stu_detail/<int:pk>',studetail,name='stud')  
    # path('list/',list,name='list')
]