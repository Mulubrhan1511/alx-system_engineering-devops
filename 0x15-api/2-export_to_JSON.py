#!/usr/bin/python3
''' makes a get request to a REST API '''
import json
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    user_data = requests.get(url + 'users/' + user_id).json()
    task_data = requests.get(url + 'todos').json()
    user_name = user_data['name']

    # Write tasks to JSON file
    tasks = []
    for task in task_data:
        if str(task['userId']) == user_id:
            tasks.append({
                'task': task['title'],
                'completed': task['completed'],
                'username': user_name
            })
        with open('{}.json'.format(user_id), mode="w") as file:
            json.dump({user_id: tasks}, file)
