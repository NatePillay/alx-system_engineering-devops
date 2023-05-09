#!/usr/bin/python3

import requests

def top_ten(subreddit):
    mclient = requests.sessions()

    mclient.headers['User-Agent'] = 'Custom User Agent for task 1'

    url = "https://www.reddit.com/r/{:s}/hot.json".format(subreddit)
    r = mclient.get(url, allow_redirects = False)
    if r.status_code == 200:
        list_hot_posts = r.json()["data"]["children"]
        for item in list_hot_posts:
            print(item['data']['title'])
        else:
            return None
