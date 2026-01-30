import json
import requests
import sys

def outputActivity(username):
    if(len(username) > 0):
        requestURL = "https://api.github.com/users/"+username+"/events"
        response = requests.get(requestURL)
        print(response.text)
        
if __name__ == "__main__":
    if (len(sys.argv) > 1):
        outputActivity(sys.argv[1])
    else:
        print("Error: No Username provided")