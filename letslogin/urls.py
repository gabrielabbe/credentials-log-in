from django.urls import path
from .views import CustomLoginView, home

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', home, name='home'),  # root URL pattern for home view
]
