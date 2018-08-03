from __future__ import absolute_import, print_function

#Import of the required libraries
import sys
import time
import zmq
import json

#Setting tweepy api up
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Creates a publisher socket with zmq that will be used to send the streamed data to logstash with a zmq subsciber
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:4321")

#Giving the following variables used by tweepy your twitter app credentials
consumer_key=""
consumer_secret=""

#Giving the following variables used by tweepy your twitter app credentials
access_token=""
access_token_secret=""

#If you would like to save the collected data as a txt file to your PC use line 28 in conjunction with line 40 & line 41
#file = open('tweepy_stream_collection.txt', 'a')

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        time.sleep(.5)
        socket.send_string("stream %s" % (data))
        print('Data Sending')
        #print(data)
        return True
        #json_data = json.dumps(data)
        #file.write(str(json_data))
        
#If there is an error with the stream this will print the status to the terminal
    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

#I set my stream filter to track buzz words associated with the wedding industry
    stream = Stream(auth, l)
    stream.filter(track=['cheese'])