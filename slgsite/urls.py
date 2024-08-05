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
from backend import views as player_view
from django.urls import include, re_path
from backend.views import index, auth_login, upload

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title = "Sign Language Game API",
      default_version = 'v1',
      description = "This is an Sign Language Game project API document.",
      terms_of_service = "https://www.google.com/policies/terms/",
      contact = openapi.Contact(email="slg_project@gmail.com"),
      license = openapi.License(name="BSD License"),
   ),
   public = True,
   permission_classes = (permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path('users/', player_view.PlayerView.as_view()),
    path("auth/login", auth_login),
    path("upload/", upload),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
