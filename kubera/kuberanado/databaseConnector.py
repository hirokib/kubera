__author__ = 'hirok_000'

import sqlite3
import os.path




class DatabaseConnector():

    def __init__(self, name):
        self.path = os.path.join(os.getcwd(), name)
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()


    def create(self):
        self.cursor.execute('''
            CREATE TABLE user(id INTEGER PRIMARY KEY, name TEXT,
                              password TEXT)'''
        )
        self.connection.commit()

    def delete(self):
        self.cursor.execute('''DROP TABLE users''')
        self.connection.commit()

    def execute(self,query):

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            self.connection.commit()
        except Exception:
            raise
        # self.connection.close()

        return result





