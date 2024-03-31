app_name = "bible_study"
from django.urls import path
from .views import CreateBibleStudyView

urlpatterns = [
    # other urls
    path("create_study/", CreateBibleStudyView.as_view(), name="create_study"),
    # other urls
]
