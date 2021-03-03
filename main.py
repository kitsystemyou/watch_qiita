import requests
import os, sys, json
import tweepy
from tweepy import OAuthHandler

auth = tweepy.OAuthHandler(os.environ["API_KEY"], os.environ["API_KEY_SECRET"])
auth.set_access_token(os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"])

api = tweepy.API(auth)

headers = {"Authorization": "Bearer " + os.environ.get("QIITA_TOKEN")}
res = requests.get("https://qiita.com/api/v2/items/5be1ed392c12cde150e4", headers=headers)

if res.status_code != 200:
    print(res.status_code, res.json())

res_data = res.json()
page_view = int(res_data["page_views_count"])

if page_view < 15000:
    tweet = "1万5千 view まであと" + str(15000 - page_view) + "view \n" + res_data["url"]
    print(tweet)
    api.update_status(status=tweet)

elif page_view >= 15000:
    tweet = "1万5千 view 達成！！" + res_data["url"]
    print(tweet)
    api.update_status(status=tweet)
print("finish job")
