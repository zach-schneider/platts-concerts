# Zac Schneider
# CSC 498

import sqlite3 

class Concertsmaster:
    """ Create a working interface to the database """
    
    def __init__(self, test=False):
        """ Make a connection to the database """
        
        if test:
            self.dbname = ":memory:"
        else:
            self.dbname = "concertsmaster.sqlite"
        
        self.conn = sqlite3.connect(self.dbname)
        
    def cursor(self):
        """ Create a cursor for the database """
        
        return self.conn.cursor()
    
    def commit(self):
        """ Commit the changes to the database """
        
        self.conn.commit()
        


db = Concertsmaster()

cursor = db.cursor()

cursor.execute("select distinct YEAR from EVENTS")

