from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *
import io
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status 



#------------------------------ BY jsonresponse 
# def stulist(request):
#     stu=StudentModel.objects.all()
#     serializer=StudentSerializer(stu,many=True)
#     return JsonResponse(serializer.data,safe=False)

# def studetail(request,pk):
#     user=StudentModel.objects.get(id=pk)
#     serializer=StudentSerializer(user)
#     return JsonResponse(serializer.data,safe=False)

# ----------------------------------- By Httpresponse
# def stulist(request):
#     stu=StudentModel.objects.all()
#     serializer=StudentSerializer(stu,many=True)
#     json_data=JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data,content_type='application/json')

# def studetail(request,pk):
#     user=StudentModel.objects.get(id=pk)
#     serializer=StudentSerializer(user)
#     json_data=JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data,content_type='application/json')
   
#------------------------------------ DESIRELIZERS----------------------------------
# def list(request):
#     if request.method =="GET":
#         user = StudentModel.objects.all()
#         serializer_data = StudentSerializer(user,many=True)
#         # print(serializer_data.data)
#         json_data = JSONRenderer().render(serializer_data.data)
#         return HttpResponse(json_data,content_type = 'application/json')
    
#     elif request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data) 
#         python_data = JSONParser().parse(stream)
#         serializer = StudentSerializer(data = python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data Created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')

# -----------------------------------multiple methods ----------------------

# def list(request):
    # if request.method =="GET":
    #     user = StudentModel.objects.all()
    #     serializer_data = StudentSerializer(user,many=True)
    #     # print(serializer_data.data)
    #     json_data = JSONRenderer().render(serializer_data.data)
    #     return HttpResponse(json_data,content_type = 'application/json')
    
    # elif request.method == 'POST': 
    #     json_data = request.body
    #     stream = io.BytesIO(json_data) 
    #     python_data = JSONParser().parse(stream)
    #     serializer = StudentSerializer(data = python_data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         res = {'msg': 'Data Created'}
    #         json_data = JSONRenderer().render(res)
    #         return HttpResponse(json_data, content_type='application/json')
    #     json_data = JSONRenderer().render(serializer.errors)
    #     return HttpResponse(json_data, content_type='application/json')
    
    # elif request.method == 'PUT':
    #     json_data = request.body
    #     stream = io.BytesIO(json_data) 
    #     python_data = JSONParser().parse(stream)
    #     id=python_data.get('id')
    #     stu=StudentModel.objects.get(id=id)
    #     serializer=StudentSerializer(stu,data=python_data)
    #     if serializer.is_valid():
    #             serializer.save()
    #             res = {'msg': 'Data Created'}
    #             json_data = JSONRenderer().render(res)
    #             return HttpResponse(json_data, content_type='application/json')
    #     json_data = JSONRenderer().render(serializer.errors)
    #     return HttpResponse(json_data, content_type='application/json')
    
    # elif request.method == 'DELETE':
    #     json_data = request.body
    #     stream = io.BytesIO(json_data) 
    #     python_data = JSONParser().parse(stream)
    #     id=python_data.get('id')
    #     if id:
    #         stu=StudentModel.objects.get(id=id)
    #         stu.delete()
    #         res={'msg':'deleted'}
    #         json_data = JSONRenderer().render(res)
    #         return HttpResponse(json_data, content_type='application/json')
    #     json_data = JSONRenderer().render(serializer.errors)
    #     return HttpResponse(json_data, content_type='application/json')

# -----------------------------------------their  endpoints-----------------------
# @csrf_exempt
# def stulist(request):
#     if request.method=='GET':
#         user = StudentModel.objects.all()
#         serializer_data = StudentSerializer(user,many=True)
#         json_data = JSONRenderer().render(serializer_data.data)
#         return HttpResponse(json_data,content_type = 'application/json')
    
#     if request.method=='POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializer = StudentSerializer(data = python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data Created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
# @csrf_exempt    
# def studetail(request,pk):
#     if request.method=='PUT':
#         user=StudentModel.objects.get(id=pk)
#         if user:
#             print(user)
#             json_data=request.body
#             stream = io.BytesIO(json_data) 
#             python_data = JSONParser().parse(stream)
#             serializer = StudentSerializer(user,data=python_data, partial = True)
#             if serializer.is_valid():
#                 serializer.save()
#                 res = {'msg': 'Data Updated'}
#                 json_data = JSONRenderer().render(res)
#                 return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
    
#     elif request.method=='DELETE':
#         user=StudentModel.objects.get(id=pk)
#         if user:
#             user.delete()
#             res = {'msg': 'Data deleted'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')

   
# --------------------------function based api-----------------------------
@api_view(['GET', 'POST']) 
def stulist(request):
    if request.method=='GET':
        user=StudentModel.objects.all()
        serializer=StudentSerializer(user,many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        serializer=StudentSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        else: return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def studetail(request,pk):
    user=StudentModel.objects.filter(id=pk)
    if user:
        if request.method=='GET':
            users=StudentModel.objects.get(id=pk) 
            serializer = StudentSerializer(users) 
            return Response(serializer.data) 
        
        elif request.method=='PUT': 
            user=StudentModel.objects.get(id=pk) 
            serializer = StudentSerializer(user,data=request.data,partial=True) 
            if serializer.is_valid(): 
                serializer.save() 
                return Response(serializer.data) 
            else: return Response(serializer.errors)

        elif request.method=='DELETE': 
                user=StudentModel.objects.get(id=pk) 
                user.delete() 
                return Response({'msg':"Data deleted successfully"}, 
                status=status.HTTP_204_NO_CONTENT)
    
    res = {'msg': 'id not present in Database'}
    return Response({'msg': 'id not present in Database'})
    





    


            
         



