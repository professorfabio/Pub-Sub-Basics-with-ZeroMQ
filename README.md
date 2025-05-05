# Pub-Sub-Basics-with-ZeroMQ

This is a very simple pub-sub app implemented with ZeroMQ. Use it as an example for the pub-sub assignment (topic-based chat system).

### First, install ZeroMQ (on each machine):

    sudo apt update

    sudo apt install python3-zmq

### Next, configure the IP address and port number of the publisher's machine in the constPS.py file

Note: Make sure that this repo is cloned in all the machines used for this experiment.

### Then, run the publisher and subscriber:

On the machine for which the IP address was configured:

    python3 publisher.py

On another machine:

    python3 subscriber.py

### Now, add other topics for in the publisher and create subscribers for the new topics.

    
