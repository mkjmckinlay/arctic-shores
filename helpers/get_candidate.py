from helpers.database import launch_query


def get_candidate(name=None, referance=None):
    user_id = launch_query(
        """SELECT id FROM candidate_candidate WHERE candidate_reference == '%s'
        AND  name == '%s'"""
        % (referance, name)
    )
    if user_id == 0:
        user_id = launch_query(
            """INSERT into candidate_candidate (candidate_reference, name) VALUES ('%s', '%s')"""
            % (referance, name))
    return user_id
