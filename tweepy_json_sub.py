import time
import json
import zmq

#data = json.loads(msg)
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt_string(zmq.SUBSCRIBE, "msg")
socket.connect("tcp://127.0.0.1:4321")
socket.send_json()

msg_in = socket.rec()
print(msg_in)

while True:
	tweet_msg = " ".join(socket.recv().split()[1:])
	tweet     = json.loads(tweet_msg)


	if "user" in tweet and "text" in tweet:
		output_tweet                  = tweet["user"]
		output_tweet["the_tweet"]     = tweet["text"]

		print(json.dumps(output_tweet))


