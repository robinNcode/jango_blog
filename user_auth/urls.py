from django.urls import path
from user_auth.views import RegisterView


urlpatterns = [
    path('register/', RegisterView.as_view()),
]
