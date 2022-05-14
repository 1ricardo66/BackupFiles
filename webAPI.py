from urllib.request import urlopen
import json

def getWebAPI():

    url = "http://localhost:8080/routers"
    response = urlopen(url)
    data = json.loads(response.read())
    print(data)
    print(type(data))
    return data

