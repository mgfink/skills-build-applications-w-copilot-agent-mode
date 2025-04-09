"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet, api_root

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

urlpatterns = [
    path('', api_root, name='root'),  # Map the root URL to api_root
    path('api/', api_root, name='api-root'),  # Custom API root
    path('api/v1/', include(router.urls)),  # Versioned API routes
    path('admin/', admin.site.urls),  # Admin endpoint
    path('api/workouts/', WorkoutViewSet.as_view({'get': 'list', 'post': 'create'}), name='workouts'),  # Direct mapping for workouts
    path('api/users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='users'),  # Direct mapping for users
    path('api/teams/', TeamViewSet.as_view({'get': 'list', 'post': 'create'}), name='teams'),  # Direct mapping for teams
    path('api/activities/', ActivityViewSet.as_view({'get': 'list', 'post': 'create'}), name='activities'),  # Direct mapping for activities
    path('api/leaderboard/', LeaderboardViewSet.as_view({'get': 'list', 'post': 'create'}), name='leaderboard'),  # Direct mapping for leaderboard
]
