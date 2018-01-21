#!/usr/bin/env python
import os, time

# import required libraries
from kafka import SimpleProducer, KafkaClient
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
#from twitter_config import consumer_key, consumer_secret, access_token, access_token_secret

KAFKA_SERVER = os.environ['kafka_server']
TWITTER_CONSUMER_KEY = os.environ['twitter_consumer_key']
TWITTER_CONSUMER_SECRET = os.environ['twitter_consumer_secret']
TWITTER_ACCESS_TOKEN = os.environ['twitter_access_token']
TWITTER_ACCESS_TOKEN_SECRET = os.environ['twitter_access_token_secret']
KAFKA_TOPIC = os.environ['kafka_topic']

# Kafka settings
topic = b'twitter-stream'

retries = 0
done = False
while not done:
    try:
        # setting up Kafka producer
        kafka = KafkaClient(KAFKA_SERVER+':9092')
        producer = SimpleProducer(kafka)
        done = True
    except:
        if retries < 5:
            retries += 1
            print "Failed to connect to kafka at '%s', retrying in 5 seconds (attempt %i)" % (KAFKA_SERVER, retries)
            time.sleep(5);
        else:
            print "Failed to connect to kafka at '%s' after %i retries, exiting" % (KAFKA_SERVER, retries)
print "connected to %s" % (KAFKA_SERVER)

#This is a basic listener that just put received tweets to kafka cluster.
class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send_messages(KAFKA_TOPIC, data.encode('utf-8'))
        #print json.loads(data).keys()
        return True

    def on_error(self, status):
        print "Error: "+status

WORDS_TO_TRACK = "trump donald potus".split()

if __name__ == '__main__':
    print 'running the twitter-stream python code'
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    stream = Stream(auth, l)
    # Goal is to keep this process always going
    while True:
        try:
            #stream.sample()
            stream.filter(languages=["en"], track=WORDS_TO_TRACK)
        except:
            pass