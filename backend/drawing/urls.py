from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="drawing-home"),
    path('workspace', views.workspace, name="drawing-workspace"),
    path('profile', views.profile, name="drawing-user-profile"),
    path('leaderboard', views.leaderboard, name="drawing-leaderboard"),
]
