import sqlite3

class SqliteStorage:
    def __init__(self, db_path):
        db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()


    def check_if_joke_exists(self, joke_id):
        pass

    def insert_joke(self, joke_id, joke_value):
        sql = ''' INSERT INTO chuck(id, value)
                  VALUES(?,?) '''
        self.cur.execute(sql, (joke_id, joke_value))