import sqlite3
from os import sys

def insertDatabase(films):
    with DBConnection("oscar.db") as db:
        filmNames = []

        for key in films.keys():
            filmNames.append(key)

        rates:float = [(i/2) for i in range(10)]

        value = 0
        films_values = []
        rating_values =[]
        for title in filmNames:
            films_values.append((title, value))
            for i in range(len(films[title])):
                rating_values.append((rates[i], films[title][i], value))
        
            value += 1

        db.cur.executemany("INSERT INTO films (title, Id) VALUES (?, ?)", films_values)
        db.con.commit()

        db.cur.executemany("INSERT INTO ratings (rate, quantity, film_id) VALUES (?, ?, ?)", rating_values)
        db.con.commit()

class DBConnection():
        def __init__(self, dbname):
            self.dbname = dbname    
        def __enter__(self):
            self.con = sqlite3.connect(self.dbname)
            self.cur = self.con.cursor()
            return self
        def __exit__(self, exc_type, exc_val, exc_tb):
            self.cur.close()
            self.con.close()
         
