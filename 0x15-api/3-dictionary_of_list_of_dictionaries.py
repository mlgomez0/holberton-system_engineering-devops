#!/usr/bin/python3
"""Using task # 0: export to JSON file for all users, using the format
   { "USER_ID": [ {"task": "TASK_TITLE", "completed":
   TASK_COMPLETED_STATUS, "username": "USERNAME"}},
   {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
   "username": "USERNAME"}}, ... ]}
"""
import json
import requests
import sys


if __name__ == "__main__":

    fl = "todo_all_employees.json"
    url_user = "https://jsonplaceholder.typicode.com/users/"
    url_todo = "https://jsonplaceholder.typicode.com/todos/"
    req_todo = requests.get(url_todo).json()
    req_user = requests.get(url_user).json()
    final_dic = {}
    for user in req_user:
        l = []
        u_id = user.get("id")
        u_n = user.get("username")
        for task in req_todo:
            if task.get("userId") == u_id:
                dic = {}
                tx = task.get("title")
                st = task.get("completed")
                dic = {'username': u_n, 'task': tx, 'completed': st}
                l.append(dic)
        final_dic[u_id] = l
    json_str = json.dumps(final_dic)
    with open(fl, mode="w", encoding='utf-8') as file_json:
        file_json.write(json_str)
