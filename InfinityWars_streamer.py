from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class TwitterStreamer():
	def __init__(self):
		pass

	def stream_tweets(self, fetched_tweets_infinity_wars, hash_tag_list):
		listener = StdOutListener(fetched_tweets_infinity_wars)
		auth = OAuthHandler('IJVdG3C0ycFV2JOqOGXgT22pV','UzzZXADlJFxDvNzkemX9b2DIvJW24l4fdd4n2fMDoP8cSmeqHH')
		auth.set_access_token('65461579-alKNjYTL1pwOqjchZbEcqTMVrZzVNYDAMFbQf5eMS','lu2iLAnFPrrTo9hsmyqDsZ0g2TLjU4NRps5UYtAtVBaYE')
		stream = Stream(auth, listener)

		stream.filter(track = hash_tag_list)


class StdOutListener(StreamListener):

	def __init__(self, fetched_tweets_infinity_wars):
		self.fetched_tweets_infinity_wars = fetched_tweets_infinity_wars

	def on_data(self, data):
		try:
			print(data)
			with open(self.fetched_tweets_infinity_wars, 'a') as tf:
				tf.write(data)
			return True
		except BaseException as e:
			print("Error on_data %s" & str(e))
		return True

	def on_error(self, status):
		print(status)

if __name__ == '__main__':
	
	hash_tag_list = ['infinity wars']
	fetched_tweets_infinity_wars = "infinitywars.json"

	twitter_streamer = TwitterStreamer()
	twitter_streamer.stream_tweets(fetched_tweets_infinity_wars, hash_tag_list)

