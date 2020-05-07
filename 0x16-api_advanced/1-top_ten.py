#!/usr/bin/python3
"""function that queries the Reddit API and returns the first 10
   hot posts for a given subreddit"""

import requests


def top_ten(subreddit):
    """uses get request to reddit url to
       get the 10 hottest posts """

    headers = {'user-agent': 'X-Modhash'}
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    get_req = requests.get(url, headers=headers, allow_redirects=False)
    get_subs = get_req.json()
    if get_req.status_code == 404:
        return (0)
    else:
        count = 0
        for post in get_subs["data"]["children"]:
            print(post["data"]["title"])
            count += 1
            if count == 10:
                break
