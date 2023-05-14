#!/usr/bin/python3
''' A module containing functions for working with the reddit api '''
import requests

url = 'https://www.reddit.com'
'''Reddit's base API URL'''


def number_of_subscribers(subreddit):
    '''ret number of subscribers from a given subreddit'''
    api_headers = {
            'Accept': 'application/json',
            'User-Agent': ''.join([
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                'AppleWebKit/537.36 (KHTML, like Gecko)',
                'Chrome/97.0.4692.71',
                'Safari/537.36',
                'Edg/97.0.1072.62'
                ])
    }

    res = requests.get(
            '{}/r/{}/about/.json'.format(url, subreddit),
            headers = api_headers,
            allow_redirects=False
    )
    if res.status_code == 200:
        return res.json()['data']['subscribers']
    return 0
