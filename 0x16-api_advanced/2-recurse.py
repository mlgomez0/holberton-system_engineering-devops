#!/usr/bin/python3
"""recursive function queries the Reddit API and returns all
   hot posts for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[], v_aft=''):
    """uses get request to reddit url to
       get all hot posts """

    h = {'user-agent': 'X-Modhash'}
    q = {'after': v_aft}
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    get_req = requests.get(url, headers=h, params=q, allow_redirects=False)
    pd = get_req.json()
    if get_req.status_code == 404:
        return (None)
    else:
        for post in pd["data"]["children"]:
            hot_list.append(post["data"]["title"])
        v_aft=pd["data"]["after"]
        if v_aft is None:
            return hot_list
        else:
            return (recurse(subreddit, hot_list, v_aft))
