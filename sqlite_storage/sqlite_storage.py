import sqlite3
from sqlite3 import Error
import datetime


class SqliteStorage:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

    def insert_joke(self, joke_id, joke_value):
        sql = ''' INSERT OR IGNORE INTO chuck(id,value,timestamp)
                VALUES(?,?,?) '''
        self.cursor.execute(sql, (joke_id, joke_value, datetime.datetime.now()))
        self.conn.commit()
    
    def check_for_duplicate(self, joke_id):
        joke_exists = False
        sql = ''' SELECT * FROM chuck WHERE id = ? '''
        self.cursor.execute(sql, (joke_id,))
        if self.cursor.fetchone():
            joke_exists = True
        else:
            joke_exists = False
        
        return joke_exists
    
    def read_all_jokes(self):
        self.cursor.execute('SELECT * FROM chuck')

        return self.cursor.fetchall()
    
