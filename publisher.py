import zmq, time, random
from constPS import * #-

context = zmq.Context()
s = context.socket(zmq.PUB)        # create a publisher socket
p = "tcp://"+HOST+":"+ PORT      # how and where to communicate
s.bind(p)                          # bind socket to the address
while True:
	time.sleep(5)                    # wait every 5 seconds
	msg = str.encode("TIME " + time.asctime())
	s.send(msg) # publish the current time

	rand = random.randint(0,1000)
	msg = str.encode("RAND " + str(rand))
	s.send(msg)
