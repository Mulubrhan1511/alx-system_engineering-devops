#!/usr/bin/python3
import requests
import sys

if __name__ == "main":
    url = "https://jsonplaceholder.typicode.com/users/"
    user_id = sys.argv[1]
    user = requests.get(url + user_id).json()
    todo = requests.get(url + user_id + "/todos").json()
    name = user.get("name")
    tasks = []
    for task in todo:
        tasks.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(name, len(tasks), len(todo)))
    for task in tasks:
        print("\t{}".format(task))
