from django.shortcuts import render
from django.views.generic.list import ListView

from candidate.models import Candidate
from scores.models import Scores


class CandidateView(ListView):
    model = Candidate
    ordering = ["name"]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        highest = Scores.objects.values_list("score").order_by("score").last()
        if highest:
            context["highest"] = highest[0]
        return context
