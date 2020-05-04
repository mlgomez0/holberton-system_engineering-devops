#!/usr/bin/python3
"""Using task # 0: export to CSV file using the format
   "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE".

"""
import json
import requests
import sys


if __name__ == "__main__":

    e_ID = sys.argv[1]
    fl = e_ID + ".json"
    q = "?completed=true&userId="
    url_user = "https://jsonplaceholder.typicode.com/users/" + e_ID
    url_todo = "https://jsonplaceholder.typicode.com/todos/?userId=" + e_ID
    url_done = "https://jsonplaceholder.typicode.com/todos/" + q + e_ID
    req_user = requests.get(url_user).json()
    req_todo = requests.get(url_todo).json()
    req_done = requests.get(url_done).json()
    u_n = req_user.get("username")
    l = []
    for task in req_todo:
        tx = task.get("title")
        st = task.get("completed")
        dic = {'task': tx, 'completed': st, 'username': u_n}
        l.append(dic)
    final_dic = {e_ID: l}
    json_str = json.dumps(final_dic)
    with open(fl, mode="a", encoding='utf-8') as file_json:
        file_json.write(json_str)
