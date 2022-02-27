from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # Login page
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # Logout page
    path('logout/', views.logout_view, name='logout'),
    # Register page
    path('register/', views.register, name='register'),
]


