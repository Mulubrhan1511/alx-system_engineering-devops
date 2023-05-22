#!/usr/bin/python3
import requests
import sys


if __name__ == '__main__':

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # Retrieve user data
    user_data = requests.get(f"{base_url}/users/{employee_id}").json()
    employee_name = user_data["name"]

    # Retrieve task data
    task_data = requests.get(f"{base_url}/todos?userId={employee_id}").json()

    # Calculate task progress
    num_completed_tasks = sum(1 for task in task_data if task["completed"])
    total_num_tasks = len(task_data)

    # Print progress report
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_num_tasks}):")
    for task in task_data:
        if task["completed"]:
            print(f"\t{task['title']}")