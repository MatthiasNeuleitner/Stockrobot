import sqlite3
from StockData import StockData

class DatabaseController:
    dbName:str

    def __init__(self,dbName):
        self.dbName=dbName


    #init a table with a PK as tableNameID 
    def insertTable(self,tableName):
        conn = sqlite3.connect(self.dbName+'.db')
        try:
            conn.execute('CREATE TABLE IF NOT EXISTS '+tableName+'('+
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

    def insertIntoTable(self,tableName, column, value, info=True):
        conn = sqlite3.connect(self.dbName+'.db', isolation_level=None)
        try:
            conn.execute('INSERT INTO '+tableName +' '+ column+' Values '+ value )
            if(info):
                print (value+" inserted successfully into "+ column)
        except:
            print(value+" could not be successfully inserted into "+ column)
            pass
        conn.close()

    def createUniqueIndex(self,tableName,index,column):
        conn = sqlite3.connect(self.dbName+'.db')
        try:
            conn.execute('CREATE UNIQUE INDEX '+index+' ON '+tableName+'('+column+');')
            print (index+" index inserted successfully onto "+ column)
        except:
            print (index+" index NOT inserted successfully onto "+ column)
            pass
        conn.close()

    def insertDataFromStock(self, symbol):
        sd = StockData()
        data = sd.getAllStockValueDataPerDay(symbol)
        self.insertTable(symbol)
        self.insertNewColumn(symbol,"Value TEXT")
        self.insertNewColumn(symbol,"Time TEXT")
        self.createUniqueIndex(symbol,'timeStamp','Time')

        for date in data.items():
            self.insertIntoTable(symbol,'(Value, Time)','('+ date[1]['SMA']+', "'+ date[0]+'")',False)
