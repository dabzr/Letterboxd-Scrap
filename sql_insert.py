import sqlite3
from os import sys

def insertDatabase(films):
    con = sqlite3.connect("oscar.db")

    cur = con.cursor()

    filmNames = []

    for key in films.keys():
        filmNames.append(key)

    rates: float = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]

    value = 0

    for title in filmNames:
        cur.execute("INSERT INTO films (title, Id) VALUES(?, ?)", [title, value])
        con.commit()
        
        for i in range(len(films[title])):
            valuesToInsert = [rates[i], films[title][i], value]
            cur.execute("INSERT INTO ratings (rate, quantity, film_id) VALUES(?, ?, ?)", valuesToInsert)
            con.commit()
        value += 1

