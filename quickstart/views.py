from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.
from django.contrib.auth.models import Group
from rest_framework import viewsets
from .serializers import UserSerializer

# def index(request):
#     return HttpResponse("Hello World")


# def Userform(request):
#     return render(request, 'index.html')


# def VarifiedData(request):
#     first_name = request.GET.get('firstName', '')
#     last_name = request.GET.get('lastName', '')
#     password = request.GET.get('password', '')
#     user.first_name = first_name
#     user.last_name = last_name
#     user.password = password
#     u = user(first_name=first_name, last_name=last_name, password=password)
#     u.save()
#     print(first_name)
#     print(last_name)
#     print(password)
#     return HttpResponse("Your Log In sucessfully")
def index(request):
    return HttpResponse("sdfas")


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
