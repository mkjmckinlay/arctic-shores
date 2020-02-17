from django.contrib import admin

from candidate.models import Candidate


class CandidateAdmin(admin.ModelAdmin):
    list_display = ["candidate_reference", "name"]
    pass


admin.site.register(Candidate, CandidateAdmin)
