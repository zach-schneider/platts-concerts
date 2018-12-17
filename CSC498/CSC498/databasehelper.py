#!/usr/bin/python
# Zac Schneider
# CSC 498

import sqlite3 
from sqlite3 import Error


class Concertsmaster:
    """ Create a working interface to the database """
    
    def __init__(self):
        """ Make a connection to the database """
        
        try:
            self.conn = sqlite3.connect("concertsmaster.sqlite")
            
        except Error as e:
            print(e)
        
    
    
    def cursor(self):
        """ Create a cursor for the database """
        
        return self.conn.cursor()
    
    def commit(self):
        """ Commit the changes to the database """
        
        self.conn.commit()
        


db = Concertsmaster()

cursor = db.cursor()

try:
    cursor.execute("SELECT * FROM EVENTS")
except UnicodeEncodeError:
    print(UnicodeEncodeError)
    

rows = cursor.fetchall()

for row in rows:
    print(row)

    
