#!/usr/bin/python3
"""for a given employee ID, returns information
about his/her To-Do list progress.
extend your Python script to export data in the JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = "https://jsonplaceholder.typicode.com/"
        user = requests.get(url + "users/{}".format(sys.argv[1])).json()
        todos = requests.get(url + "todos",
                             params={"userId": sys.argv[1]}).json()

        with open("{}.json".format(sys.argv[1]), "w", newline="") as jsonfile:
            todo = []
            for t in todos:
                todo.append({
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": user.get("username")
                })
            json.dump({sys.argv[1]: todo}, jsonfile)
