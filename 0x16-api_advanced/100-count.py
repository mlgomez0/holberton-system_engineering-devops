#!/usr/bin/python3
"""recursive function that queries the Reddit API, parses
   the title of all hot articles, and prints a sorted
   count of given keywords (case-insensitive,
   delimited by spacesrecursive) """

import requests


def count_words(subreddit, word_list, v_aft=''):
    """uses get request to reddit url to
       get keyword in hot posts """

    h = {'user-agent': 'X-Modhash'}
    q = {'after': v_aft}
    s1 = "https://www.reddit.com/r/"
    word_list.sort()
    for key in word_list:
        url = s1 + subreddit + "/search.json?q=title:" + key + "&sort=hot"
        get_req = requests.get(url, headers=h, params=q, allow_redirects=False)
        if get_req.status_code == 404 or get_req.status_code == 302:
            return None

        pd = get_req.json()
        count = 0
        for post in pd["data"]["children"]:
            count = count + post["data"]["title"].lower().count(key)
        if count != 0:
            print("{} : {}".format(key, count))
"""
            v_aft = pd["data"]["after"]
            if v_aft is None:
                if count != 0:
                    print("{} : {}".format(key, count))
            else:
                return (count_words(subreddit, word_list, v_aft)) """
