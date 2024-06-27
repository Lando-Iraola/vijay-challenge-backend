from django.urls import path
from . import views
from .views import PostView
from .views import PostDetail


urlpatterns = [
    path('posts/', PostView.as_view()),
    path('posts/<int:pk>', PostDetail.as_view())
]
