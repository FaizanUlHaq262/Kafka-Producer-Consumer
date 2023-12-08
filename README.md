# Kafka-Producer-Consumer
This uses multiple producers and multiple consumers to test concepts of kafka
# Note
This repository assumes you already have kafka installed in your system and have set it up

## Description
This Kafka-based data processing system is designed to handle various financial data streams, including user portfolios, tax calculations, and fraud detection. The system uses Kafka for message queuing and MongoDB for data storage, ensuring efficient processing and storage of financial data.

## Files in the Repository
1. `topics.py`: Script to create Kafka topics.
2. `userPortfolio9093.py`: Kafka Consumer for processing user portfolio data.
3. `tax9094.py`: Kafka Consumer for calculating taxes.
4. `fraud9092.py`: Kafka Consumer for fraud detection.
5. `run.sh`: Bash script to start Kafka servers and run Python scripts.
6. `ratesProducer.py`: Kafka Producer for generating and sending financial rates.

## Installation
To set up this project, follow these steps:
1. Install Kafka and set up the Kafka servers.
2. Install MongoDB and run the MongoDB server.
3. Ensure Python is installed with required libraries: `kafka-python` and `pymongo`.
4. Clone this repository to your local machine.
5. run the requirements.txt to install all the necessary libraries

## Usage
1. Start the Kafka servers using the `run.sh` script.
2. Execute `topics.py` to create the necessary Kafka topics.
3. Run `userPortfolio9093.py`, `tax9094.py`, and `fraud9092.py` to start the respective Consumers.
4. Run `ratesProducer.py` to start the Producer that sends financial rates to Consumers.

### Example
To process user portfolio data, the `userPortfolio9093.py` consumer will listen to the 'userportfolio' topic and calculate the BTC a person can buy according to their portfolio.

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
