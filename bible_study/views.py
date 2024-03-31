from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BibleStudyForm
from .models import BibleStudy


class CreateBibleStudyView(LoginRequiredMixin, View):
    template_name = "bible_study/create_study.html"

    def get(self, request, *args, **kwargs):
        form = BibleStudyForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = BibleStudyForm(request.POST)
        if form.is_valid():
            study = form.save(
                commit=False
            )  # Save the form temporarily without committing to the database
            study.user = request.user  # Set the study's user to the current user
            study.save()  # Now save the study to the database
            return redirect("some_view_name")  # Redirect to a new URL
        return render(request, self.template_name, {"form": form})
