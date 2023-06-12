from django.urls import path, include


urlpatterns = [
    path('user_auth/', include('user_auth.urls')),
]
