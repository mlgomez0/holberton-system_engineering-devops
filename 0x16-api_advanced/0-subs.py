#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers
   for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """uses get request to reddit url to
       get the subscribers number """

    headers = {'user-agent': 'X-Modhash'}
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    get_req = requests.get(url, headers=headers, allow_redirects=False)
    get_subs = get_req.json()
    if get_req.status_code == 404:
        return (0)
    else:
        return (get_subs["data"]["subscribers"])
