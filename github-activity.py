import json
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
            "repo": event["repo"]
        }
        if parsed["type"] == "WatchEvent":
            print("Test")
    

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        outputActivity(sys.argv[1])
    else:
        print("Error: No Username provided")