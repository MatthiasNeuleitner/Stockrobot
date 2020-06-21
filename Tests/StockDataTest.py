def main():
        sd = StockData()
        print(sd.getStockValueByDatePerMinute("2020-06-19 15:56","GOOGL"))

if __name__ == "__main__":
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        # import  your stuff here. Python wont allow import in an higher orden than his own directory. So we trick it
        from StockData import StockData
        from DatabaseController import DatabaseController
        from StockData import StockData
    else:
        from ..StockData import StockData
        from ..DatabaseController import DatabaseController
        from ..StockData import StockData
    main()