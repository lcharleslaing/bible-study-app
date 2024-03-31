app_name = "bible_study"
from django.urls import path
from .views import (
    CreateBibleStudyView,
    BibleStudyListView,
    BibleStudyDetailView,
)  # Make sure to import BibleStudyListView

urlpatterns = [
    path(
        "", BibleStudyListView.as_view(), name="bible_study_list"
    ),  # Add this line for the landing page
    path("create_study/", CreateBibleStudyView.as_view(), name="create_study"),
    path("study/<int:pk>/", BibleStudyDetailView.as_view(), name="study_detail"),
]
