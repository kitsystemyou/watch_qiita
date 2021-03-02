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
print(res_data["id"])
print(res_data["page_views_count"])
print(res_data["url"])

page_view = int(res_data["page_views_count"])

if page_view < 10000:
    print(10000 - page_view)
    tweet = "1万 view まであと" + str(10000 - page_view) + "view !\n" + res_data["url"]
    print(tweet)
    api.update_status(status=tweet)
    print("sudoori")

elif page_view == 10000:
    tweet = "1万 view 達成！！" + res_data["url"]
    api.update_status(status=tweet)
    print(tweet)
else:
    pass
print("end")
