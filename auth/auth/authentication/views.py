from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Signup
@api_view(["POST"])
def Signup(request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()

    return Response("Signup Successfull")
