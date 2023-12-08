#-----Importing Libraries-----#
from kafka import KafkaProducer
import json
import time
import requests
from datetime import datetime 


#-----MAIN GENERATOR-----#
if __name__ == "__main__":
    
    producer = KafkaProducer(
        bootstrap_servers = ['localhost:9092','localhost:9093']
        )
    
    url = r'https://api.coinbase.com/v2/exchange-rates?currency=BTC'        #url to get bitcoin exchange rates
    response = requests.get(url)        #gets the response from the url and keeps it updates as it is a live feed
    rates = response.json()
    rates = rates['data']['rates']    #extracting the rates dictionary from the response
    
    countries = list()
    for i,(k,v) in enumerate(rates.items()):       #extracting al the available countries from the api
        if i ==155:
            break
        else:
            countries.append(k)    
    tempDict = {                #stores them in a dictionary
        "Countries":countries
    }
    
    i=0
    while i!=10:     #the producer runs a total of 5 times
        response = requests.get(url)        #gets the response from the url and keeps it updates as it is a live feed
        rates = response.json()
        rates = rates['data']['rates']    #extracting the rates dictionary from the response
        
        producer.send('rates',key = b'rates',value = json.dumps(rates).encode('utf-8'))        #send the exchange rates to the userportfolio consumer   
        producer.send('tax',key = b'rates',value = json.dumps(tempDict).encode('utf-8'))               #send the available countries to the tax consumer
        print(f'Sending Exchange Rates To Consumer at port 9093 & 9092  at {datetime.now()}')
        # print(rates)
        time.sleep(32)
        i+=1
        
    producer.flush()
    producer.close()