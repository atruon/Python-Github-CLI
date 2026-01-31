import json
from weakref import ref
import requests
import sys

def outputActivity(username):
    requestURL = "https://api.github.com/users/"+username+"/events"
    response = requests.get(requestURL)
    if (response.status_code == 404):
        print("Error: Invalid Username")
        return
    parsed_events = []
    events = response.json()
    for event in events:
        parsed = {
            "type": event["type"],
            "actor": event["actor"],
            "repo": event["repo"],
            "payload": event["payload"],
            "name": event["repo"]["name"]
        }
        if parsed["type"] == "WatchEvent":
            parsed_events.append("Started on " + parsed["name"])
        elif parsed["type"] == "PushEvent":
            parsed_events.append("Pushed commits to " + parsed["name"])
        elif parsed["type"] == "CreateEvent":
            parsed_events.append("Created repo - " + parsed["name"] + ". Description: " +
                                 parsed["payload"]["description"] )
        elif parsed["type"] == "ForkEvent":
            parsed_events.append(parsed["actor"]["display_login"] + " " + parsed["payload"]["action"] +
                                 " " + parsed["payload"]["forkee"]["full_name"])
    return parsed_events

def printParsedEvents(arr):
    for string in arr:
        print(string)

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        allEvents = outputActivity(sys.argv[1])
        printParsedEvents(allEvents)
    else:
        print("Error: No Username provided")