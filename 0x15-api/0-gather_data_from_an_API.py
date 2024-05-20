#!/usr/bin/python3
"""for a given employee ID, returns information about his/her To-Do list progress."""
import requests
import sys

if __name__ == "__main__":
     if len(sys.argv) > 1:
        url = "https://jsonplaceholder.typicode.com/"
        user = requests.get(url + "users/{}".format(sys.argv[1])).json()
        todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

        completed = []
        for todo in todos:
            if todo.get("completed") is True:
                completed.append(todo.get("title"))
        print("Employee {} is done with tasks({}/{}):".format(
            user.get("name"), len(completed), len(todos)))
        for c in completed:
            print("\t {}".format(c))
