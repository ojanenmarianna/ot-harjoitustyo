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

        cursor.execute("SELECT * FROM Scores ORDER BY score DESC LIMIT 10")

        high_scores = cursor.fetchall()

        return high_scores

    def add_new_win(self, name):
        cursor = self._connection.cursor()
        score = cursor.execute('SELECT score FROM Scores WHERE name=?', [name]).fetchone()
        if score is None:
            cursor.execute(
                    "INSERT INTO Scores (name, score) VALUES (?, ?)",
                    (name, 1)
        )
        else:
            cursor.execute("UPDATE Scores SET score=score+1 WHERE name=?", [name])

        self._connection.commit()

score_repository = ScoreRepository(get_database_connection())
scores = score_repository.find_all()
