"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static

# 配置 OpenAPI 信息 (简化版)
schema_view = get_schema_view(
    openapi.Info(
        title="MyProject API",  # API 的标题
        default_version="v1",  # API 的版本
        description="API for managing customer and Copilot integration",  # 简短描述
        contact=openapi.Contact(email="your_email@example.com"),  # 联系人信息 (可选)
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # 公开访问
)

urlpatterns = [
path('admin/', admin.site.urls),
path("", include("myapp.urls")),
path('api/', include('myapp.urls')),  # 应用 API 路由
path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),  # OpenAPI JSON
]

