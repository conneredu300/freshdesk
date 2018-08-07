import requests
import json
import pandas as pd
from sklearn.cluster import KMeans

class Freshdesk:
    api_key = ""
    domain = ""
    password = ""

    def __init__(self,apikey,domain,password):
        self.api_key = apikey
        self.domain = domain
        self.password = password


    def returnAllTickets(self):
        # Return the tickets that are new or opend & assigned to you
        # If you want to fetch all tickets remove the filter query param
        r = requests.get("https://"+ self.domain +".freshdesk.com/api/v2/tickets?filter=new_and_my_open", auth = (self.api_key, self.password))
        if r.status_code == 200:
          return prepareTickets(r)

        print("x-request-id : " + r.headers['x-request-id'])
        print("Código : " + str(r.status_code))


def prepareTickets(data):
    data = data.json()
    dataset = pd.
    head = dataset.head()