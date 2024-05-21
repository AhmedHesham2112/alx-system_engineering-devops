#!/usr/bin/python3
"""for a given employee ID, returns information
about his/her To-Do list progress.
extend your Python script to export data in the JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w", newline="") as jsonfile:
        all = dict()
        for user in users:
            id = user.get("id")
            todos = requests.get(url + "todos",
                                 params={"userId": id}).json()
            todo = []
            for t in todos:
                todo.append({"username": user.get("username"),
                             "task": t.get("title"),
                             "completed": t.get("completed")})
            all[id] = todo
        json.dump(all, jsonfile)
