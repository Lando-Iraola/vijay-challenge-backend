from django.urls import path
from . import views
from .views import PostView


urlpatterns = [
    path('posts/', PostView.as_view())
]
