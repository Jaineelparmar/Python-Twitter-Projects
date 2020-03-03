import json
import requests
import operator
from requests_oauthlib import OAuth1
from collections import Counter

api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' # enter api key
api_secret_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' #enter api secret key
auth = OAuth1(api_key, api_secret_key) #authenticating the keys

screen_name = 'narendramodi' # search keyword (twitter handle)
url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+screen_name+"&count=200"
ans = requests.get(url, auth=auth)
j_tweet = json.loads(ans.text) 


z = []
for x in range(1, 200):
	y = j_tweet[x]['text']
	z.append(y)



tweet_string = ""
for tweet in z:
	tweet_string = tweet_string+tweet
tweet_words = tweet_string.split(" ") #creating a list of words
tweet_words_count = Counter(tweet_words)



b=[]
for x in tweet_words: 
	b.append(tweet_words_count[x])
key_max = max(b)
max_word = [key for key,value in tweet_words_count.items() if value == key_max]  #items() - In Python Dictionary, items() method is used to return the list with all dictionary keys with values.

print("The most commonly used word is: "+str(max_word))