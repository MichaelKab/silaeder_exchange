from django.urls import path

from .views import SignUpView

urlpatterns = [
    path('signupsdsd/', SignUpView.as_view(), name=''),
]