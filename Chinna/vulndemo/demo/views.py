from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .models import User
from django.contrib.auth import authenticate, login as auth_login


# ❌ Broken Authentication
def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username, password=password)
            return HttpResponse(f"Welcome, {user.username}")
        except:
            return HttpResponse("Invalid credentials")
    return render(request, "demo/login.html")

# ❌ SQL Injection
def search_customer(request):
    name = request.GET.get('name', '')
    query = f"SELECT * FROM demo_customer WHERE name = '{name}'"
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return HttpResponse(f"Results: {result}")

# ❌ XSS
def show_name(request):
    name = request.GET.get("name", "")
    return render(request, "demo/show_name.html", {"name": name})