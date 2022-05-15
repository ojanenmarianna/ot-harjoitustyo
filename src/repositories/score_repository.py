from re import S
from database_connection import get_database_connection

class ScoreRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute("select * from scores")

        rows = cursor.fetchall()

        return rows

    def find_top_ten(self):
        cursor = self._connection.cursor()

        cursor.execute('SELECT * FROM Scores ORDER BY score DESC LIMIT 10')

        high_scores = cursor.fetchall()

        return high_scores

score_repository = ScoreRepository(get_database_connection())
scores = score_repository.find_all()