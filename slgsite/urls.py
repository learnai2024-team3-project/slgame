"""
URL configuration for slgsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from backend.player_view import PlayerView
from django.urls import include, re_path
from backend.views import index, wordle_view, tutorial_view
from backend.auth_login_view import auth_login, log_in_view, log_out_view
from backend.upload_view import upload
from backend.game_start_view import game_start
from backend.submit_game_view import submit_game

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Sign Language Game API",
      default_version='v1',
      description="This is an Sign Language Game project API document.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="slg_project@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index) ,
    path("wordle/", wordle_view, name='wordle'),    
    path('tutorial/', tutorial_view, name='tutorial'),
    path('players/', PlayerView.as_view()),
    path("auth/login", auth_login),
    path("login/", log_in_view),
    path("logout/", log_out_view),
    path("upload/", upload),
    path("game/start", game_start),
    path("game/submit", submit_game),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            view=schema_view.without_ui(cache_timeout=0),
            name='schema-json'
            ),
    re_path(r'^swagger/$',
            view=schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'
            ),
    re_path(r'^redoc/$',
            view=schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'
            ),
    path('accounts/', include('allauth.urls')),
]
