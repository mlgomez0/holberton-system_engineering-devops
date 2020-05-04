#!/usr/bin/python3
"""Uses REST API (https://jsonplaceholder.typicode.com/)
   for a given employee ID, returns information about his/her
   TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":

    e_ID = sys.argv[1]
    q = "?completed=true&userId="
    url_user = "https://jsonplaceholder.typicode.com/users/" + e_ID
    url_todo = "https://jsonplaceholder.typicode.com/todos/?userId=" + e_ID
    url_done = "https://jsonplaceholder.typicode.com/todos/" + q + e_ID
    req_user = requests.get(url_user).json()
    req_todo = requests.get(url_todo).json()
    req_done = requests.get(url_done).json()
    s = "Employee {} is done with tasks({}/{}):"
    print(s.format(req_user.get("name"), len(req_done), len(req_todo)))
    for task in req_done:
        print("	 {}".format(task.get("title")))
