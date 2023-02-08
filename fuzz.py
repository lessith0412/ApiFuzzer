import requests
import sys

def loop():
    for words in sys.stdin:
        res = requests.get(url = f"https://j17lt.csb.app/{words}")
        if res.status_code == 404:
            loop()
        else:
            print(res.status_code)
            data = res.json()
            print(data)
            print(words)
loop()
