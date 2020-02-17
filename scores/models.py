from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Scores(models.Model):
    candidate_id = models.ForeignKey('candidate.Candidate',
                                     on_delete=models.CASCADE
                                     )
    score = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
    )

    # class Meta:
    #