import requests
from sk import *

api_address ="https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=0c5bf6600fbd40dda0cceda2b036a522"
json_data = requests.get(api_address).json()

ar=[]
def news ():
    for i in range (3):
        ar.append("number "+ str(i+1) +" , " + json_data["articles"][i]["title"]+".")
    return ar


