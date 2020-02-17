import csv
import json
import os

from arctic.settings.settings import PROJECT_PATH


with open(os.path.join(PROJECT_PATH, 'files/candidates.json')) as handle:
    jsonlist = json.loads(handle.read())
    sortedlist = sorted(jsonlist, key=lambda k: k['score'])

with open(os.path.join(PROJECT_PATH, 'files/sorted.csv'), 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['candidate_ref', 'name', 'score'])
    for line in sortedlist:
        writer.writerow([line['candidate_ref'], line['name'], line['score']])

