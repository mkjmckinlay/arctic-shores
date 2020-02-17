from django.contrib import admin

from scores.models import Scores


class ScoreAdmin(admin.ModelAdmin):
    list_display = ["candidate_id", "score"]


admin.site.register(Scores, ScoreAdmin)
