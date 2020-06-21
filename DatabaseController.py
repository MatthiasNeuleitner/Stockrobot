import sqlite3

class DatabaseController:
    dbName:str

    def __init__(self,dbName):
        self.dbName=dbName


    #init a table with a PK as tableNameID 
    def insertTable(self,tableName):
        conn = sqlite3.connect(self.dbName+'.db')
        try:
            conn.execute('CREATE TABLE '+tableName+'('+
            tableName+'ID INTEGER PRIMARY KEY)')
            print (tableName+" created successfully!")
        except:
            print("Could not create table:\t"+tableName)
            print(tableName+ " exists already?")
            pass
        conn.close()
    
    def insertNewColumn(self,tableName, column):
        conn = sqlite3.connect(self.dbName+'.db')
        try:
            conn.execute('ALTER TABLE '+tableName+ ' ADD ' +column+'')
            print (column+" added successfully to "+tableName)
        except:
            print("Could not alter table.")
            print("Column " +column + " exits already?")
            pass
        conn.close()

    def dropTable(self,tableName):
        conn = sqlite3.connect(self.dbName+'.db')
        try:
            conn.execute('DROP TABLE '+tableName)
            print (tableName+" deleted successfully!")
        except:
            pass
        conn.close()