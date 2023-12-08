# Kafka-Producer-Consumer
This uses multiple producers and multiple consumers to test concepts of kafka

# Setup
Extract all the files in one place

Run the zookeeper using the command: `bin/zookeeper-server-start.sh config/zookeeper.properties` 

Run each broker in a seperate terminal using the commands:

`bin/kafka-server-start.sh config/server1.properties` retention period 1 day

`bin/kafka-server-start.sh config/server2.properties`   retention period 7 days

`bin/kafka-server-start.sh config/server3.properties`   retention period 30 days

Now open a new terminal and run the `topics.py` file using the command:

`python3 topics.py` this shall create the topics needed.

Next run the producers in different terminals using the commands:

`python3 portfolioProducer.py` This producer will be randomly generating user portfolios which includes their names, income, age and country

`python3 ratesProducer.py` This producer will be calling a bitcoing exchange rate api and gives us a dictionary full of BTC exchange rates will several currencies

Now run the consumers in different terminals using the commands:

`python3 fraud9092.py`  This consumer processes the user portfolios and finds out if the user is a fraud or is eligible to buy bitcoin

`python3 userPortfolio9093.py`  This consumer takes in the exchange rates data and portfolio data and calculates how much bitcoin the person can buy 

`python3 tax9094.py`    This consumer takes in the portfolio data and calculates how much tax return the user owes 
