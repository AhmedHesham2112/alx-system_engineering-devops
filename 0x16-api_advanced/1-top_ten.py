#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit. If no results are found
for the given subreddit, the function should return None.
"""
import requests


def top_ten(subreddit):
    """
    recursive function that queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit. If no results are found
    for the given subreddit, the function should return None.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "script by u/medo_hesham"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json()['data']['subscribers']
        return 0
    except Exception as e:
        return 0
