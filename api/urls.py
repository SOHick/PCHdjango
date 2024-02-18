"""
URL configuration for timetracker project.

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
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter

from api.views import main_view, TimeslotModelViewSet, TagsViewSet

router = SimpleRouter()
router.register("timeslots", TimeslotModelViewSet, basename="timeslots")
router.register("tags", TagsViewSet, basename="tags")

urlpatterns = [path("", main_view), path("token/", obtain_auth_token), *router.urls]