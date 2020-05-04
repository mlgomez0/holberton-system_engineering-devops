#!/usr/bin/python3
"""Using task # 0: export to CSV file using the format
   "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE".
"""
import requests
import sys
import csv


if __name__ == "__main__":

    e_ID = sys.argv[1]
    fl = e_ID + ".csv"
    q = "?completed=true&userId="
    url_user = "https://jsonplaceholder.typicode.com/users/" + e_ID
    url_todo = "https://jsonplaceholder.typicode.com/todos/?userId=" + e_ID
    url_done = "https://jsonplaceholder.typicode.com/todos/" + q + e_ID
    req_user = requests.get(url_user).json()
    req_todo = requests.get(url_todo).json()
    req_done = requests.get(url_done).json()
    u_n = req_user.get("username")
    for task in req_todo:
        st = task.get("completed")
        tx = task.get("title")
        with open(fl, mode="a", encoding='utf-8') as f:
            p = csv.QUOTE_ALL
            e_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=p)
            e_writer.writerow([e_ID, u_n, st, tx])
