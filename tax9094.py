# Description: This Consumer is used to figure out how much Tax will be imposed on the person.

#-----Importing Libraries-----#
from kafka import KafkaConsumer
import json
import time
import random
import pymongo

#-----MAIN GENERATOR-----#
if __name__ == "__main__":
    
    consumer = KafkaConsumer(
        'tax',
        bootstrap_servers = ['localhost:9094'],     #will only access data from the topic tax on port 9094
        auto_offset_reset='latest'
        )

    #starting our mongoDB client
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    #creating a database
    db = client['taxDataBase']
    #Create a collection (same as table in SQL)
    taxDataBase = db['taxCollection']
    print("MongoDB Connected ;)")
    
    taxRecords = (random.randint(3, 18))/100

    for message in consumer:
        if message.key == b'portfolio':
            portfolio = message.value.decode('utf-8')
            portfolio = json.loads(portfolio)
            
            imposableTax = portfolio['Income'] * taxRecords
            portfolio['TaxReturn'] = imposableTax
            print(portfolio)    
            
            #mongoDB code
            db.taxCollection.insert_one(portfolio)
        
    consumer.close()