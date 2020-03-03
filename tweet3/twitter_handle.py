import json
import requests
from requests_oauthlib import OAuth1

api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # enter api key
api_secret_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # enter api secret key
auth = OAuth1(api_key, api_secret_key) #authenticating the keys


def keyword_handler(keyword):

    url = "https://api.twitter.com/1.1/search/tweets.json?q="+keyword+"&count=200&tweet_mode=extended&lang=en&result_type=popular"

    response = requests.get(url, auth=auth)
    # print(response, response.text, type(response.text))

    j_tweet = json.loads(response.text)
    # print(j_tweet, type(j_tweet))

    for x in j_tweet['statuses']:
        print(x['full_text'])


# search keyword
keyword_handler('python language')