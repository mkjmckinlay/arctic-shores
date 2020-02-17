import sqlite3
from sqlite3 import Error
from arctic.settings.settings import PROJECT_PATH
import os


def create_connection():
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(os.path.join(PROJECT_PATH, "db.sqlite3"))
    except Error as e:
        print(e)
    return conn


def launch_query(query):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(query)
    if query.find("SELECT") != -1:
        result = cur.fetchall()
        if result:
            return result[0][0]
        else:
            return 0
    if query.find("INSERT") != -1:
        conn.commit()
        return cur.lastrowid


def update(query):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
