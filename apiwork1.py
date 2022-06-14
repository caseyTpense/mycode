import requests
from pprint import pprint
#3rd party

url= "https://opentdb.com/api.php?amount=1&category=18&type=multiple"

#send a request to this api
#GET -- give me some info
#PUT -- change the info
# POST-- add this info
#DELETE-- delete the info

resp= requests.get(url)

# resp is holding our response from the api

trivia= resp.json()

print(trivia["results"][0]["question"])

