from django.urls import path
from .views import *

# urlpatterns = [
#     path('stu_list/',stulist,name='stu'),
#     path('stu_detail/<int:pk>',studetail,name='stud')  
#     # path('list/',list,name='list')
# ]


# -------------------------class based 
urlpatterns=[
    path('stulist/', Stulist.as_view()),
    path('studetail/<int:pk>/',Studetail.as_view())
    
]