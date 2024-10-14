"""
URL configuration for segmine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from rest_framework import permissions, routers

from django.conf import settings
from django.conf.urls.static import static

from catalogs.viewsets import CatalogViewSet
from courses.viewsets import CourseViewSet
from evaluations.viewsets import EvaluationViewSet
from locations.viewsets import CountryViewSet, DepartmentViewSet
from sites.viewsets import SiteViewSet
from students.viewsets import StudentViewSet, UserViewSet
from surveys.viewsets import SurveyViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from accounts.views import RegisterApiView

router = routers.DefaultRouter()
router.register(r"catalogs", CatalogViewSet)
router.register(r"courses", CourseViewSet)
router.register(r"evaluations", EvaluationViewSet)
router.register(r"surveys", SurveyViewSet)

router.register(r"countries", CountryViewSet)
router.register(r"departments", DepartmentViewSet)

router.register(r"sites", SiteViewSet)
router.register(r"students", StudentViewSet)
router.register(r"users", UserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterApiView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
