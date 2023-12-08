#-----Importing Libraries-----#
from kafka import KafkaProducer
import json
import time
import requests
from datetime import datetime 
from faker import Faker
import random
import requests

#-----MAIN GENERATOR-----#
if __name__=="__main__":   
    
    producer = KafkaProducer(
    bootstrap_servers=['localhost:9092','localhost:9093', 'localhost:9094']      #will only send data to consumer that estimates how much bitcoin can a person buy && to consumer that estimates how much Tax is on that person
    )
    
    url = r'https://api.coinbase.com/v2/exchange-rates?currency=BTC'        #calls an api for exchange rates
    response = requests.get(url)        #gets the response from the url and keeps it updates as it is a live feed
    rates = response.json()

    countries = list()
    for i,(k,v) in enumerate(rates['data']['rates'].items()):       #extracting all the available countries from the api
        if i ==155:
            break
        else:
            countries.append(k)
    
    counter = 0
    n=10
    while counter != n:    #the producer runs a total of 10 times
        name=Faker().name()
        age=Faker().random_int(min=10, max=85, step=random.randint(1,6))  #an age of 10 to 85 with step also being totally random
        country=random.choice(countries)        #randomly assign a country to the person
        income=Faker().random_int(min=1000, max=600000, step=random.randint(1000,50000))  #an income of 1000 to 600000 with step also being totally random

        portfolio ={
            'Name':name,
            'Age':age,
            'Country':country,
            'Income':income
        }
        
        producer.send('userportfolio', key = b'portfolio',value = json.dumps(portfolio).encode('utf-8'))   #sending data to the topic userportfolio
        producer.send('fraud', key = b'portfolio',value = json.dumps(portfolio).encode('utf-8'))   #sending data to the topic fraud on port 9092
        producer.send('tax', key = b'portfolio',value = json.dumps(portfolio).encode('utf-8'))   #sending data to the topic tax
        print(f'Sending Portfolios To Consumer at port 9093, 9092 & 9094 at {datetime.now()}')       #keeps a track of the portfolio being produced in producer terminal
       
        time.sleep(32)   #sleeps for 32 second
        counter+=1
        
    producer.flush()    #ensures all data has been sent to the broker before closing the connection
    producer.close()