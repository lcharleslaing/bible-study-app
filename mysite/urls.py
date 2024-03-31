from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

import bible_study

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("", TemplateView.as_view(template_name="homepage.html"), name="homepage"),
    path("bible-study/", include("bible_study.urls", namespace="bible_study")),
]
