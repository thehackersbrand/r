from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.profile_view, name='profile'),
]