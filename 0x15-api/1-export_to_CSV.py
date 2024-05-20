#!/usr/bin/python3
"""for a given employee ID, returns information
about his/her To-Do list progress.
extend your Python script to export data in the JSON format."""
import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = "https://jsonplaceholder.typicode.com/"
        user = requests.get(url + "users/{}".format(sys.argv[1])).json()
        todos = requests.get(url + "todos",
                             params={"userId": sys.argv[1]}).json()

        with open("{}.csv".format(sys.argv[1]), "w", newline="") as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for todo in todos:
                writer.writerow([sys.argv[1], user.get("username"),
                                todo.get("completed"), todo.get("title")])
