from helpers.database import launch_query


def add_score(candidate_id = None, score = None):
    launch_query(
        """INSERT into scores_scores (candidate_id_id, score) VALUES (%s, %s)"""
        % (candidate_id, score))
