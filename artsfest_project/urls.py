from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path("admin/", admin.site.urls),

    path("", include("dashboard.urls")),

    path("students/", include("students.urls")),

    path("events/", include("events.urls")),

    path("participants/", include("participants.urls")),

    path("results/", include("results.urls")),

    path("", include("django.contrib.auth.urls")),

]