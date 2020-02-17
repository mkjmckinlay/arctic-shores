import os
import csv
import re

from arctic.settings.settings import PROJECT_PATH
from helpers.get_candidate import get_candidate
from helpers.add_score import add_score

with open(os.path.join(PROJECT_PATH, "files/candidates.csv")) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    next(csv_reader)
    for row in csv_reader:
        candidate_reference = row[0]
        candidate_name = row[1]
        candidate_score = float(row[2])
        if len(candidate_reference) == 8 and re.match(
            "^[A-Za-z0-9_-]*$", candidate_reference
        ):
            if 0 <= candidate_score <= 100:
                candidate_id = get_candidate(candidate_name, candidate_reference)
                add_score(candidate_id, candidate_score)
                print(
                    f"reference - {candidate_reference} score - {candidate_score} added"
                )
            else:
                print(
                    f"reference - {candidate_reference} score - {candidate_score} is invalid "
                )
        else:
            print(f"reference - {candidate_reference} is invalid")
