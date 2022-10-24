from http.client import responses
from urllib import request
import requests
responses = requests.get("https://www.usom.gov.tr/url-list.txt", verify = False)
dosya = open("usom.txt" ,"w")
dosya.write(str(responses.content))
dosya.close()