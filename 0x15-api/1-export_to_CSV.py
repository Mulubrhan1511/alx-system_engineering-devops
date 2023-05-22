#!/usr/bin/python3
''' makes a get request to a REST API '''
import csv
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    user_data = requests.get(url + 'users/' + user_id).json()
    task_data = requests.get(url + 'todos').json()
    user_name = user_data['name']

    with open('{}.csv'.format(user_id), mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in task_data:
            if str(task['userId']) == user_id:
                writer.writerow([user_id, user_name,
                                str(task['completed']), task['title']])
