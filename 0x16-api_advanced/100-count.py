#!/usr/bin/python3
"""
recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
"""
import requests
from collections import Counter
import re


def count_words(subreddit, word_list, after=None, word_count=None):
    if word_count is None:
        word_count = Counter()
    """
    recursive function that queries the Reddit API,
    parses the title of all hot articles,
    and prints a sorted count of given keywords
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "script by u/medo_hesham"
    }
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json()
    posts = data['data']['children']

    word_list = [word.lower() for word in word_list]

    for post in posts:
        title = post['data']['title'].lower()
        words = re.findall(r'\b\w+\b', title)
        for word in word_list:
            word_count[word] += words.count(word)
    after = data['data']['after']

    if after is not None:
        return count_words(subreddit, word_list, after, word_count)

    if word_count:
        for word, count in sorted(word_count.items(),
                                  key=lambda item: (-item[1], item[0])):
            if count > 0:
                print(f"{word}: {count}")
