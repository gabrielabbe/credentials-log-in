from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import path

class CustomLoginView(LoginView):
    template_name = 'login.html'

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('', home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
