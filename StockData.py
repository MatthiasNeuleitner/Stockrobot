import json
import requests

class StockData: 
    key = 'GCVZOA2YSVHS2MYQ'
    
    #only input correct date time... or i hate you ex. :"2020-06-19 15:56" wont work with todays date 
    # symbol like IBM GOOGL MSFT
    #TODO: get the date for right now from google or other source...
    def getStockValueByDatePerMinute(self,date,symbol):
        r = requests.get('https://www.alphavantage.co/query?function=SMA&symbol='+symbol+'&interval=1min&time_period=50&series_type=open&apikey='+self.key)
        data = json.loads(json.dumps(r.json()))
        return data['Technical Analysis: SMA'][date]['SMA']
    
    