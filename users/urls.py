from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login_view.as_view(), name='user_login'),
    path('logout/', views.user_logout_view.as_view(), name='user_logout'),
    
]
