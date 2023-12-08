#!/bin/bash

set -e


#starting server1
gnome-terminal --tab --title="server1" --command="bash -c 'cd /home/hdoop/kafka; ./bin/kafka-server-start.sh ./config/server1.properties; sleep 5'"
sleep 4
#starting server2
gnome-terminal --tab --title="server2" --command="bash -c 'cd /home/hdoop/kafka; ./bin/kafka-server-start.sh ./config/server2.properties; sleep 10'"
sleep 4
#starting server3
gnome-terminal --tab --title="server3" --command="bash -c 'cd /home/hdoop/kafka; ./bin/kafka-server-start.sh ./config/server3.properties; sleep 15'"
sleep 4

#Create Topics
gnome-terminal --tab --title="Topics" --command="bash -c 'python3 topics.py; sleep 5'"
sleep 5
#Turn on Consumers
gnome-terminal --tab --title="userPortfolio9093" --command="bash -c 'exec python3 userPortfolio9093.py; sleep 10'"
gnome-terminal --tab --title="tax9094" --command="bash -c 'exec python3 tax9094.py; sleep 10'"
gnome-terminal --tab --title="fraud9092" --command="bash -c 'exec python3 fraud9092.py; sleep 10'"
sleep 2
#Turn on Producers
gnome-terminal --tab --title="ratesProducer" --command="bash -c 'exec python3 ratesProducer.py; sleep 10'"
gnome-terminal --tab --title="portfolioProducer" --command="bash -c 'exec python3 portfolioProducer.py; sleep 10'"