import json
import requests
from requests_oauthlib import OAuth1

api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX' # enter api key.
api_secret_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' # enter api secret key.
auth = OAuth1(api_key, api_secret_key)

username = "ENTER THE USERNAME HERE"

# you can give the count as per the number of tweets you want to see.
url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+username+"+&count=10"

# Will ssend a GET request.
response = requests.get(url, auth=auth)

#Will get response in json.
j_response = json.loads(response.text)

for text in j_response:
    print(text["text"])
    print("\n")
   

# username : msdhoni or Cristiano