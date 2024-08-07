from django.urls import path
from .views import *

# urlpatterns = [
#     path('stu_list/',stulist,name='stu'),
#     path('stu_detail/<int:pk>',studetail,name='stud')  
#     # path('list/',list,name='list')
# ]


# -------------------------class based 
# urlpatterns=[
#     path('stulist/', Stulist.as_view()),
#     path('studetail/<int:pk>/',Studetail.as_view())   
# ]

# ------------------------------MIXINS BASWD URL--------------------------------
# urlpatterns =[
#     path('stulist/', Stulist.as_view()),
#     path('studetail/<int:pk>/',Studetail.as_view()) 
#]


#------------------------------ Routerss url -------------------------------
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', Studentviewset, basename='user')
urlpatterns = router.urls