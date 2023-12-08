# Description: This Consumer is used to figure out how much BTC can person buy according to their portfolio.

#-----Importing Libraries-----#
from kafka import KafkaConsumer
import json
import time
import random
import pymongo
#-----MAIN GENERATOR-----#
if __name__ == "__main__":
    
    pConsumer = KafkaConsumer(
        'userportfolio',
        bootstrap_servers = ['localhost:9093'],     #will only access data from the topic userportfolio on port 9093
        auto_offset_reset='latest'
        )
    
    rConsumer = KafkaConsumer(
        'rates',
        bootstrap_servers = ['localhost:9093'],     #will only access data from the topic userportfolio on port 9093
        auto_offset_reset='latest'
        )

    #starting our mongoDB client
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    #creating a database
    db = client['portfolioDataBase']
    #Create a collection (same as table in SQL)
    portfolioDataBase = db['userPortfolio']
    print("MongoDB Connected ;)")
    
    
    for pmessages,rmessages in zip(pConsumer,rConsumer):

        if pmessages.key == b'portfolio':       #if the key is portfolio then decode the value and store it in portfolio
            portfolio = ( pmessages.value.decode('utf-8'))
            portfolio = json.loads(portfolio)
            
        if rmessages.key == b'rates':           #if the key is rates then decode the value and store it in rates
            rates = rmessages.value.decode('utf-8')
            rates = json.loads(rates)
               
        if portfolio['Country'] in rates.keys():    #if the country of the user is in the rates dictionary then calculate how much btc can he buy according to his exchange rate
            buyable_BTC = int(portfolio['Income']) / float(rates[portfolio['Country']])
            portfolio['BTC'] = buyable_BTC
            print(portfolio)       
            
            #mongoDB code
            db.userPortfolio.insert_one(portfolio)
        else:
            print('not working')
    
    pConsumer.close()
    rConsumer.close()