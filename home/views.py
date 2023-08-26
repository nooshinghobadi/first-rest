from django.shortcuts import render
from django.http import HttpRequest,JsonResponse
from todo.models import Todo
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

def index_page(request):
 context={
  'todos':Todo.objects.order_by('priority').all()
 }
 return render(request,'home/index.html',context)

#def todos_json(request:HttpRequest):
 todos= list(Todo.objects.order_by('priority').all().values('title','is_done'))
 return JsonResponse({'todos':todos})

@api_view(['GET'])
def todos_json(request:Request):
 todos= list(Todo.objects.order_by('priority').all().values('title','is_done'))
 return Response({'todos':todos} , status.HTTP_200_OK)