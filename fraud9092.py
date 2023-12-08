# Description: This Consumer is used to figure out if person is a fraud or not. It is connected to the topic fraud on port 9092. 

#-----Importing Libraries-----#
from kafka import KafkaConsumer
import json
import time
import random
import pymongo
#-----MAIN GENERATOR-----#
if __name__ == "__main__":
    
    consumer = KafkaConsumer(
        'fraud',
        bootstrap_servers = ['localhost:9092'],     #will only access data from the topic fraud on port 9092
        auto_offset_reset='latest'
        )
    
    #starting our mongoDB client
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    #creating a database
    db = client['FraudDataBase']
    #Create a collection
    FraudDataBase = db['FraudCollection']
    print("MongoDB Connected ;)")

    for message in consumer:
        if message.key == b'portfolio':
            message = message.value.decode('utf-8')
            portfolio = json.loads(message)
            if portfolio['Age']<18 or portfolio['Income'] < 150000:     #if the age is less than 18 then the person is a minor and is not allowed to buy bitcoin
                name = portfolio['Name']
                print(f'{name} is a fraud and is not allowed to buy bitcoin')
                print('ALERT PERSONNEL!!!')
                
                #mongoDB code
                temp = {            #temp stores the data that will be inserted into the database
                    name:"is a fraud and is not allowed to buy bitcoin"
                }
                db.FraudCollection.insert_one(temp)
            else:
                name = portfolio['Name']
                print(f'{name} No fraud detected')
                temp = {            #temp stores the data that will be inserted into the database
                    name:"is not a fraud"
                }
                db.FraudCollection.insert_one(temp)
                
        else:
            print('Data from Unknown Port!')
    consumer.close()