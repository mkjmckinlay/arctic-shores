from django.db import models
from scores.models import Scores


class Candidate(models.Model):
    name = models.TextField()
    candidate_reference = models.CharField(max_length=8, unique=True)

    def get_scores(self):
        scores = (
            Scores.objects.filter(candidate_id=self.id)
            .order_by("score")
            .values_list("score", flat=True)
        )
        return list(scores)

    def __str__(self):
        return f"{self.name} - {self.candidate_reference}"
