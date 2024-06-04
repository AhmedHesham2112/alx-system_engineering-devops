#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "script by u/medo_hesham"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        posts = response.json()['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
