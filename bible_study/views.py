from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView
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
            study = form.save(commit=False)
            study.user = request.user  # Automatically link the logged-in user
            study.save()
            # Use the correct URL name for redirection
            return redirect("bible_study:bible_study_list")
        return render(request, self.template_name, {"form": form})


class BibleStudyListView(ListView):
    model = BibleStudy
    template_name = "bible_study/studies_list.html"  # Make sure this template exists
    context_object_name = "studies"

    def get_queryset(self):
        # Adjust this method according to how you want to filter studies
        return BibleStudy.objects.filter(
            user=self.request.user
        )  # Assumes you want to show studies of the logged-in user


class BibleStudyDetailView(DetailView):
    model = BibleStudy
    template_name = "bible_study/study_detail.html"
    context_object_name = "study"
