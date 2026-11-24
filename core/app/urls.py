
from django.urls import path
from app.views import ProfileView,ProfilePost

urlpatterns = [
    path('get/',ProfileView.as_view()),
    path('post/',ProfilePost.as_view())
]

